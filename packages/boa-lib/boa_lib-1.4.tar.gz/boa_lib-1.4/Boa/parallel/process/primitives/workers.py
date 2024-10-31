"""
This module defines Process subclasses used to create worker processes.
"""

import sys
from abc import abstractmethod
from enum import IntEnum
from subprocess import Popen
from typing import Any, Callable, Generator, Iterable, Iterator, ParamSpec, TypeVar

from ....pipes import Duplex, PipeWriter
from ...abc import Worker as AbstractWorker
from ...thread.future import Future
from ..environment import Environment
from .process import Process

__all__ = ["PythonChild", "Worker"]





class RemoteException(Exception):

    """
    This class of exception indicates that an exception occured in a worker process. It is used to re-raise this exception in the parent process.
    """
            




P = ParamSpec("P")
R = TypeVar("R")
Y = TypeVar("Y")
S = TypeVar("S")

class PythonChild(Process):

    """
    This abstract subclass of process will create a Python child process using the same executable as the currently running Python interpreter.
    Subclasses must override the "run" method in order to use such a class.
    """

    from ....parallel import logger as __logger

    __FLAGS = IntEnum("__FLAGS", (
        "TERMINATE",
        "GET_ENV",
        "SET_ENV",
        "REMOTE_THREAD"
    ))

    __ACTIONS : dict[IntEnum, tuple[Callable[["PythonChild", Duplex], Any] | None, Callable[[Duplex], None] | None]] = {}

    __slots__ = {
        "__process" : "The Popen object representing this process",
        "__pipe" : "The duplex used to communicate with this process",
        "__pid" : "The PID of the Python child process",
        "__env" : "The local copy of the child's environment",
        "__action_lock" : "An RLock on the actions to submit to the child",
        "__next_result" : "A Future to the result of the ongoing action in the child process",
        "__death_lock" : "A lock used to ensure all pipes to the child are closed when its death is detected",
        "__died" : "A boolean set to True when the death watcher acknoledges child death"
    }

    __Future = Future
    
    def __init__(self) -> None:
        from os import getpid
        from pickle import dumps
        from threading import RLock

        from ....pipes import bridge
        from ...thread.primitives import NephilimThread
        from ..environment import local_env
        self.__process, w, close = self.__spawner()

        # For now, the bridge is not confidential :
        # anyone who has access to the underlying shared array will be able to read what was shared.

        with open(w, "wb", closefd=False) as pipe:

            parent_pipe, child_pipe = bridge()

            data = dumps(child_pipe)

            pipe.write(len(data).to_bytes(8, "little"))
            pipe.write(data)
            pipe.flush()

            assert parent_pipe.read(1) == b"\1", "Child process had a connection error."
        
        close()
        self.__pipe = parent_pipe
        self.__pid = int.from_bytes(parent_pipe.read(8), "little")
        super().__init__()
        def del_pid(p):
            self.__pid = None
        self.add_callback(del_pid)
        parent_pipe.write(getpid().to_bytes(8, "little"))
        
        self.__pipes_to_close : list["Duplex"] = [self.__pipe, child_pipe]

        def close_all_pipes(tp : "NephilimThread | Process"):
            with self.__action_lock:
                for pipe in self.__pipes_to_close:
                    pipe.close()
                self.__pipes_to_close.clear()

        self.add_callback(close_all_pipes)
        self.__action_lock = RLock()
        self.__env = local_env
        with self.__action_lock:
            NephilimThread(target = self.__handle_child, fall_callback = close_all_pipes, name = "Python Child Handler Thread").start()
            self.environment = local_env
        
        self.__logger.debug(f"{self} initialized")

    def __get_parent_action(self, flag : int) -> Callable[[Duplex], Any] | None:
        """
        Internal function that returns a function that the parent process should call when receiving this flag from its child.
        """
        if flag not in self.__ACTIONS:
            raise ValueError(f"Received an unknown flag from PythonChild process : '{flag}'")
        action = self.__ACTIONS[flag][0]
        if action:
            return action.__get__(self)     # Artificially bind the method to the instance.
    
    @staticmethod
    def _get_child_action(flag : int) -> Callable[[Duplex], None] | None:
        """
        Internal function that returns a function that the child process should call when receiving this flag from its parent.
        """
        if flag not in PythonChild.__ACTIONS:
            raise ValueError(f"Received an unknown flag from parent process : '{flag}'")
        return PythonChild.__ACTIONS[flag][1]

    def __handle_child(self):
        """
        Internal function used to handle the connection to the child.
        """
        with self.__pipe.read_lock:

            while True:

                try:
                    flag = self.__pipe.read(1)[0]
                except:
                    return

                action = self.__get_parent_action(flag)
                result = None
                if action:
                    result = action(self.__pipe)
                if self.__next_result:
                    fut, self.__next_result = self.__next_result, None
                    fut.set(result)
    
    if sys.platform == "win32":

        # Yes on windows, you have to create the pipe "manually", because os.pipe() is useless...instead of fd, we use handles

        def __spawner(self) -> tuple[Popen, int, Callable[[], None]]:
            """
            Internal function to spawn the worker process. 
            Returns a Popen object, a file descriptor to a writing pipe to communicate with the child and a function to call to close the pipe.
            """
            from msvcrt import open_osfhandle
            from os import environ, getpid
            from subprocess import Popen
            from sys import executable
            from _winapi import CloseHandle, CreatePipe
            r, w = CreatePipe(None, 0)
            wfd = open_osfhandle(w, 0)
            proc = Popen(args=[executable, "-m", "Boa.parallel.process.primitives.python_process", str(r), str(getpid())], env=environ.copy())
            return proc, wfd, lambda : CloseHandle(r) and CloseHandle(w)

    else:

        def __spawner(self) -> tuple[Popen, int, Callable[[], None]]:
            """
            Internal function to spawn the worker process.
            Returns a Popen object,  a file descriptor to a writing pipe to communicate with the child and a function to call to close the pipe.
            """
            from os import close, environ, getpid, pipe
            from subprocess import Popen
            from sys import executable
            r, w = pipe()
            proc = Popen(args=[executable, "-m", "Boa.parallel.process.primitives.python_process", str(r), str(getpid())], executable=executable, env=environ.copy(), pass_fds=[r])
            return proc, w, lambda : close(r) and close(w)
        
    @property
    def pid(self) -> int | None:
        return self.__pid
            
    @staticmethod
    def __terminate_child(p : Duplex):
        """
        Internal function for the child to take cleanup actions when receiving the termination order.
        """
        with p.write_lock:
            p.write(bytes([PythonChild.__FLAGS.TERMINATE]))
        exit()

    def terminate(self):
        with self.__action_lock:
            self.__next_result = fut = self.__Future()
            self.__pipe.write(bytes([self.__FLAGS.TERMINATE]))
            fut.wait()

    __ACTIONS[__FLAGS.TERMINATE] = (None, __terminate_child)

    def __get_env_parent(self, p : Duplex):
        """
        Internal function used by the parent to request the environment of its child.
        """
        from Viper.pickle_utils import WhiteListUnpickler

        from ..environment import EnvDict, Environment
        unp = WhiteListUnpickler()
        d_new : EnvDict = (unp << p)
        d_old = self.__env.export()
        if d_new != d_old:
            self.__env.unregister(self)
            self.__env = Environment()
            self.__env.copy_from(d_new)
            self.__env.register(self)
        return self.__env

    @staticmethod
    def __get_env_child(p : Duplex):
        """
        Internal function used by the child to send its environment to its parent.
        """
        from Viper.pickle_utils import StreamPickler

        from ..environment import local_env
        p << bytes([PythonChild.__FLAGS.GET_ENV])
        p << StreamPickler(local_env.export())
    
    @staticmethod
    def __set_env_child(p : Duplex):
        """
        Internal function used by the child to change its environment to what its parent sent.
        """
        from Viper.pickle_utils import WhiteListUnpickler

        from .. import environment
        unp = WhiteListUnpickler()
        unp.allow(environment.Environment)
        environment.local_env.copy_from(unp << p)
        p << bytes([PythonChild.__FLAGS.SET_ENV])

    __ACTIONS[__FLAGS.GET_ENV] = (__get_env_parent, __get_env_child)
    __ACTIONS[__FLAGS.SET_ENV] = (None, __set_env_child)

    @property
    def environment(self) -> Environment:
        with self.__action_lock:
            self.__next_result = fut = self.__Future()
            self.__pipe.write(bytes([self.__FLAGS.GET_ENV]))
            return fut.result()
    
    @environment.setter
    def environment(self, env : Environment):
        from Viper.pickle_utils import StreamPickler

        from ..environment import Environment
        if not isinstance(env, Environment):
            raise TypeError(f"Expected Environment, got '{type(env).__name__}'")
        with self.__action_lock:
            self.__env.unregister(self)
            self.__env = env
            env.register(self)
            self.__next_result = fut = self.__Future()
            self.__pipe.write(bytes([self.__FLAGS.SET_ENV]))
            self.__pipe << StreamPickler(env.export())
            fut.wait()

    class RemoteThread:

        """
        Internal class used to execute some functions in a DaemonThread started in the worker process.
        """

        def __init__(self, pipe : Duplex) -> None:
            from threading import Lock
            self.__pipe = pipe
            self.__lock = Lock()

        def execute(self, func : Callable[P, R], *args : P.args, **kwargs : P.kwargs) -> R:
            """
            Executes a function in the remote thread.
            Waits for its completion and returns the result.
            """
            from traceback import TracebackException
            from typing import Any, Literal

            from Viper.pickle_utils import StreamPickler, StreamUnpickler
            from Viper.abc.io import IOClosedError
            if self.__pipe.closed:
                raise IOClosedError("Remote thread has exited")
            with self.__lock:
                self.__pipe << StreamPickler((func, args, kwargs))
                result : tuple[Literal[True], Any] | tuple[Literal[False], TracebackException] = StreamUnpickler() << self.__pipe
                if result[0]:
                    return result[1]
                else:
                    error_str = "".join(result[1].format())
                    raise RemoteException(f"The following exception occured in the remote thread:\n\n{error_str}")

        def exit(self):
            """
            Stops the remote thread.
            """
            from sys import exit

            from Viper.pickle_utils import StreamPickler
            with self.__lock:
                if self.__pipe.closed:
                    from Viper.abc.io import IOClosedError
                    raise IOClosedError("Remote thread has exited")
                self.__pipe << StreamPickler((exit, (), {}))
                with self.__pipe.readable as n:
                    if n:
                        raise RuntimeError("Remote thread was not closed properly")

        @property
        def alive(self) -> bool:
            """
            Indicates if the remote thread is still running.
            """
            return not self.__pipe.closed
        
        @alive.setter
        def alive(self, value : bool):
            if not isinstance(value, bool):
                raise TypeError(f"Expected bool, got '{type(value).__name__}'")
            if value == True and not self.alive:
                raise ValueError("Cannot resuscitate RemoteThread")
            if value != self.alive:
                self.exit()

        @property
        def busy(self) -> bool:
            """
            Indicates if the remote thread is currently being used.
            """
            return self.__lock.locked()
        
        def __del__(self):
            if self.alive:
                self.exit()

    @staticmethod   
    def __remote_thread_child(p : Duplex):
        """
        Internal function used by the child process to start a remote thread.
        """
        from traceback import TracebackException

        from Viper.abc.io import IOClosedError
        from Viper.pickle_utils import StreamPickler, StreamUnpickler

        from ....pipes import Duplex
        from ...thread.primitives import DaemonThread
        def run(p : Duplex):
            try:
                while True:
                    try:
                        func, args, kwargs = StreamUnpickler() << p
                        res = func(*args, **kwargs)
                        data = (True, res)
                    except SystemExit:
                        p.close()
                        raise
                    except BaseException as e:
                        data = (False, TracebackException.from_exception(e))
                    try:
                        p << StreamPickler(data)
                    except BaseException as e:
                        data = (False, TracebackException.from_exception(e))
                        p << StreamPickler(data)
            except IOClosedError:
                pass
        p_thread : Duplex = StreamUnpickler() << p
        PythonChild.__remote_thread_child_N += 1
        DaemonThread(target=run, args=(p_thread, ), name=f"RemoteThread #{PythonChild.__remote_thread_child_N}").start()

    __remote_thread_child_N = 0

    __ACTIONS[__FLAGS.REMOTE_THREAD] = (None, __remote_thread_child)

    def create_remote_thread(self) -> RemoteThread:
        """
        Creates a remote thread in the worker process. Returns a RemoteThread object.
        This object can be used to run functions remotely.
        """
        from Viper.pickle_utils import StreamPickler

        from ....pipes import bridge
        with self.__action_lock:
            if not self.alive:
                raise RuntimeError("Worker process is dead")
            self.__logger.debug(f"Initializing remote thread in {self}")
            parent_dup, child_dup = bridge()
            self.__pipe << bytes([self.__FLAGS.REMOTE_THREAD])
            self.__pipe << StreamPickler(child_dup)
            self.__pipes_to_close.append(parent_dup)
            self.__pipes_to_close.append(child_dup)
            return self.RemoteThread(parent_dup)





class Worker(PythonChild, AbstractWorker):

    """
    This Process subclass is used to submit jobs.
    """

    from ...exceptions import FutureSetError as __FutureSetError
    from ....parallel import logger as __logger
    from ....pipes import pipe
    from Viper.pickle_utils import StreamPickler as __StreamPickler, StreamUnpickler as __StreamUnpickler
    __pipe = staticmethod(pipe)
    del pipe

    __slots__ = {
        "__remote_thread" : "A unique remote thread object created to execute tasks in this worker process",
        "__task_count" : "The number of tasks this worker has already executed"
    }

    def __init__(self) -> None:
        from threading import Lock

        super().__init__()
        self.__remote_thread = self.create_remote_thread()
        self.__lock = Lock()
        self.__task_count : int = 0

    @property
    def task_count(self) -> int:
        return self.__task_count

    @property
    def busy(self) -> bool:
        return self.__remote_thread.busy
    
    @property
    def alive(self) -> bool:
        try:
            return self.__remote_thread.alive
        except AttributeError:
            return super().alive

    def execute_async_into(self, fut : Future[R], func: Callable[P, R], *args: P.args, **kwargs: P.kwargs):
        from threading import Event

        from ...thread.primitives import DaemonThread

        started = Event()

        def wait_for_result():
            try:
                with self.__lock:
                    started.set()
                    self.__logger.debug(f"Sending task '{(func, args, kwargs)}' to {self}'s remote thread")
                    res = self.__remote_thread.execute(func, *args, **kwargs)
                    self.__task_count += 1
                try:
                    fut.set(res)
                    self.__logger.debug(f"Set result of '{(func, args, kwargs)}' computed by {self} into {fut}")
                except* self.__FutureSetError:
                    self.__logger.info(f"Could not set result of '{(func, args, kwargs)}' computed by {self} into {fut}")
            except BaseException as e:
                try:
                    fut.set_exception(e)
                    self.__logger.debug(f"Set exception of '{(func, args, kwargs)}' computed by {self} into {fut}")
                except* self.__FutureSetError:
                    self.__logger.info(f"Could not set exception of '{(func, args, kwargs)}' computed by {self} into {fut}")
        
        DaemonThread(target = wait_for_result, name = f"Worker Watcher Thread for {fut}").start()
        started.wait()
        
        return fut
    
    @staticmethod
    def _run_iterator(iterable : Iterable[Y], pipe : PipeWriter):
        """
        Internal function used to compute the elements of an iterable in a remote worker.
        """
        iterator = iter(iterable)
        pipe << b"\1"
        while True:
            try:
                message = (True, next(iterator))
            except BaseException as e:
                message = (False, e)
            try:
                pipe << Worker.__StreamPickler(message)
            except:
                pass
            if not message[0]:
                return
    
    def execute_async_iterator(self, iterable: Iterable[Y]) -> Iterator[Y]:
        reader, writer = Worker.__pipe()
        
        def remote_iterator():
            try:
                validated = False
                while not validated:
                    acquired = reader.readable.acquire(False, 0.001)
                    if acquired:
                        if reader.readable:
                            yield reader.read(1)
                            validated = True
                    if not validated and fut.is_set:        # This means the worker could not even start the iterator.   
                        return
                while True:
                    try:
                        ok, res = Worker.__StreamUnpickler() << reader
                    except RuntimeError:
                        return
                    if ok:
                        yield res
                    else:
                        if not isinstance(res, StopIteration):
                            raise res
                        else:
                            return
            finally:
                reader.close()
        
        fut = self.execute_async(Worker._run_iterator, iterable, writer)
        r = remote_iterator()
        try:
            next(r)     # To ensure remote iterator was started and it is ready!
        except BaseException as e:
            if fut.is_set and fut.exception:
                raise fut.exception from None
            raise e from None
        return r
    
    class RemoteGenerator(Generator[Y, S, R]):

        """
        This class is used to handle generators ran in a worker process.
        """

        import enum
        ACTIONS = enum.IntEnum("ACTIONS", ("NEXT", "SEND", "THROW", "CLOSE", "YIELD", "ERROR", "RETURN"))
        from ....pipes import bridge
        __bridge = staticmethod(bridge)
        from Viper.pickle_utils import StreamUnpickler as __StreamUnpickler, StreamPickler as __StreamPickler
        from threading import Lock as __Lock
        del enum, bridge

        def __init__(self, gen : Generator[Y, S, R] | Callable[P, Generator[Y, S, R]], worker : "Worker", args : P.args, kwargs : P.kwargs) -> None:
            self.__lock = Worker.RemoteGenerator.__Lock()
            self.__pipe, child_pipe = Worker.RemoteGenerator.__bridge()
            self.__worker = worker
            fut = self.__worker.execute_async(Worker._run_generator, gen, child_pipe, args, kwargs)
            validated = False
            while not validated:
                acquired = self.__pipe.readable.acquire(False, 0.001)
                if acquired:
                    if self.__pipe.readable:
                        self.__pipe.read(1)
                        validated = True
                if not validated and fut.is_set and fut.exception:        # This means the worker could not even start the iterator.   
                    raise fut.exception

        def __iter__(self) -> Generator[Y, S, R]:
            return self

        def __next__(self) -> Y:
            if not self.__lock.acquire(False):
                raise ValueError("generator already executing")
            try:
                self.__pipe << bytes([Worker.RemoteGenerator.ACTIONS.NEXT])
                f = self.__pipe.read(1)[0]
                match f:
                    case Worker.RemoteGenerator.ACTIONS.YIELD:
                        return Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.ERROR:
                        raise Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.RETURN:
                        e = StopIteration()
                        e.value = Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                        raise e
                    case f:
                        raise RuntimeError(f"Received unknwown flag from remote generator : {f}")
            finally:
                self.__lock.release()

        def send(self, value: S) -> Y:
            if not self.__lock.acquire(False):
                raise ValueError("generator already executing")
            try:
                self.__pipe << bytes([Worker.RemoteGenerator.ACTIONS.SEND])
                self.__pipe << Worker.RemoteGenerator.__StreamPickler(value)
                f = self.__pipe.read(1)[0]
                match f:
                    case Worker.RemoteGenerator.ACTIONS.YIELD:
                        return Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.ERROR:
                        raise Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.RETURN:
                        e = StopIteration()
                        e.value = Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                        raise e
                    case f:
                        raise RuntimeError(f"Received unknwown flag from remote generator : {f}")
            finally:
                self.__lock.release()
        
        def throw(self, exc : BaseException):
            if not self.__lock.acquire(False):
                raise ValueError("generator already executing")
            try:
                if not isinstance(exc, BaseException):
                    raise TypeError(f"Expected BaseException, got '{type(exc).__name__}'")
                self.__pipe << bytes([Worker.RemoteGenerator.ACTIONS.THROW])
                self.__pipe << Worker.RemoteGenerator.__StreamPickler(exc)
                f = self.__pipe.read(1)[0]
                match f:
                    case Worker.RemoteGenerator.ACTIONS.YIELD:
                        return Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.ERROR:
                        raise Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                    case Worker.RemoteGenerator.ACTIONS.RETURN:
                        e = StopIteration()
                        e.value = Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                        raise e
                    case f:
                        raise RuntimeError(f"Received unknwown flag from remote generator : {f}")
            finally:
                self.__lock.release()
                
        def close(self):
            if not self.__lock.acquire(False):
                raise ValueError("generator already executing")
            try:
                self.__pipe << bytes([Worker.RemoteGenerator.ACTIONS.CLOSE])
                f = self.__pipe.read(1)[0]
                match f:
                    case Worker.RemoteGenerator.ACTIONS.YIELD:
                        Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                        raise RuntimeError("generator ignored GeneratorExit")
                    case Worker.RemoteGenerator.ACTIONS.ERROR:
                        e = Worker.RemoteGenerator.__StreamUnpickler() << self.__pipe
                        if not isinstance(e, GeneratorExit | StopIteration):
                            raise RuntimeError("generator ignored GeneratorExit")
                    case Worker.RemoteGenerator.ACTIONS.RETURN:
                        raise RuntimeError("generator ignored GeneratorExit")
                    case f:
                        raise RuntimeError(f"Received unknwown flag from remote generator : {f}")
            finally:
                self.__lock.release()
                
        def __del__(self):
            self.close()
            self.__pipe.close()

    @staticmethod
    def _run_generator(generator : Generator[Y, S, R] | Callable[P, Generator[Y, S, R]], pipe : Duplex, args : P.args, kwargs : P.kwargs):
        """
        Internal function used to compute the elements of a generator in a remote worker.
        """
        if callable(generator):
            generator = generator(*args, **kwargs)
        pipe << b"\1"
        while True:
            try:
                action : "Worker.RemoteGenerator.ACTIONS" = pipe.read(1)[0]
            except:
                return
            match action:
                case Worker.RemoteGenerator.ACTIONS.NEXT:
                    try:
                        y = next(generator)
                        res = (Worker.RemoteGenerator.ACTIONS.YIELD, y)
                    except StopIteration as e:
                        res = (Worker.RemoteGenerator.ACTIONS.RETURN, e.value)
                    except BaseException as e:
                        res = (Worker.RemoteGenerator.ACTIONS.ERROR, e)
                case Worker.RemoteGenerator.ACTIONS.SEND:
                    s : "S" = Worker.__StreamUnpickler() << pipe
                    try:
                        y = generator.send(s)
                        res = (Worker.RemoteGenerator.ACTIONS.YIELD, y)
                    except StopIteration as e:
                        res = (Worker.RemoteGenerator.ACTIONS.RETURN, e.value)
                    except BaseException as e:
                        res = (Worker.RemoteGenerator.ACTIONS.ERROR, e)
                case Worker.RemoteGenerator.ACTIONS.THROW:
                    e = Worker.__StreamUnpickler() << pipe
                    try:
                        y = generator.throw(e)
                        res = (Worker.RemoteGenerator.ACTIONS.YIELD, y)
                    except StopIteration as e:
                        res = (Worker.RemoteGenerator.ACTIONS.RETURN, e.value)
                    except BaseException as e:
                        res = (Worker.RemoteGenerator.ACTIONS.ERROR, e)
                case Worker.RemoteGenerator.ACTIONS.CLOSE:
                    try:
                        y = generator.close()
                        raise GeneratorExit
                    except BaseException as e:
                        res = (Worker.RemoteGenerator.ACTIONS.ERROR, e)
                case f:
                    raise RuntimeError(f"Unknown flag received by remote generator : {f}")
            try:
                pipe << bytes([res[0]])
                pipe << Worker.__StreamPickler(res[1])
            except:
                return
            
    def execute_async_generator(self, generator: Generator[Y, S, R] | Callable[P, Generator[Y, S, R]], *args : P.args, **kwargs : P.kwargs) -> Generator[Y, S, R]:
        return Worker.RemoteGenerator(generator, self, args, kwargs)





del P, R, Y, S, sys, abstractmethod, IntEnum, Popen, Any, Callable, ParamSpec, TypeVar, Generator, Iterable, Iterator, PipeWriter, Duplex, AbstractWorker, Future, Environment, Process