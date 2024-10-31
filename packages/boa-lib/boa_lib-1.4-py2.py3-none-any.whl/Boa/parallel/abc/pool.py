"""
This module sets up the abstract Pool system, with its joinded scheduler.
Go to other Boa.parallel packages to find their implementations.
"""

from abc import ABCMeta, abstractmethod
from collections import deque
from threading import Event, Lock
from types import TracebackType
from typing import Callable, Generator, Generic, Iterable, Iterator, ParamSpec, Protocol, TypeVar, overload
from weakref import ref
from .future import Future

__all__ = ["Worker", "Pool"]





P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
Y = TypeVar("Y")
S = TypeVar("S")

closing = False

class Worker:

    """
    The Worker Protocol describes classes used to start the execution of a task, which returns a Future to the result of the task.
    """

    @abstractmethod
    def execute_async_into(self, fut : Future[R], func : Callable[P, R], *args : P.args, **kwargs : P.kwargs):
        """
        Classes that match the Worker protocol must provide this method to execute a given function and set its result into the given Future.
        """
        raise NotImplementedError
    
    def execute_async(self, func: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> Future[R]:
        """
        Starts the execution of the given function into the worker and returns a Future to the result of the function.
        """
        from ..thread import Future
        fut = Future()
        self.execute_async_into(fut, func, *args, *kwargs)
        return fut

    @abstractmethod
    def execute_async_iterator(self, iterable : Iterable[Y]) -> Iterator[Y]:
        """
        Starts the execution of the given iterable into the worker and returns an iterator that yields the computed elements of the iterable.
        """
        raise NotImplementedError
    
    @overload
    @abstractmethod
    def execute_async_generator(self, generator : Generator[Y, S, R]) -> Generator[Y, S, R]:
        ...
    
    @overload
    @abstractmethod
    def execute_async_generator(self, generator : Callable[P, Generator[Y, S, R]], *args : P.args, **kwargs : P.kwargs) -> Generator[Y, S, R]:
        ...
    
    @abstractmethod
    def execute_async_generator(self, generator, *args, **kwargs):
        """
        Starts the execution of the given generator into the worker and returns a generator that yields the computed elements of the generator.
        Send and throw also work remotely.
        """
        raise NotImplementedError

    @abstractmethod
    def kill(self) -> None:
        """
        Classes that match the Worker protocol must provide this method to cancel the execution of a task by killing themselves.
        """
        raise NotImplementedError
    
    @property
    @abstractmethod
    def busy(self) -> bool:
        """
        A boolean value indicating if the Worker is currently busy executing a task.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def task_count(self) -> int:
        """
        The number of tasks that this worker has already executed.
        """
        raise NotImplementedError
    




module_ready = Event()
pool_manager_ready = Event()
W = TypeVar("W", bound=Worker)
class DefaultCallback(Protocol):
    
    """
    This is just a type annotation for a callable that takes an optional Future object as only argument (or no argument).
    """

    def __call__(self, fut : Future | None = None) -> None:
        ...

class Pool(Generic[W], metaclass = ABCMeta):

    """
    This is the abstract base class for Pool objects.
    A Pool represents a set of worker objects that can be used to execute multiple tasks.

    maxsize represents the maximum number of workers to keep alive at the same time. Defaults to the number of CPUs on the running machine.
    If given, the keyword argument lazy controls whether workers are spawned only when necessary or as soon as possible.
    The max_tasks_per_child argument specifies how many tasks Workers spawned by the Pool can run before being retired and replaced by a new Worker.
    
    They can also be used in context managers (with Pool() as p:). In that case, the Pool is closed when leaving the context.
    """

    from ..exceptions import FutureSetError as __FutureSetError, CancelledFuture as __CancelledFuture
    from ..thread.primitives import DaemonThread as __DaemonThread
    from ..thread.synchronization import PLock as __PLock
    from ...parallel import logger as __logger
    from threading import RLock as __RLock, Event as __Event
    from weakref import ref as __ref, WeakKeyDictionary as __WeakKeyDictionary
    from collections import deque as __deque

    __ref_holder : "__WeakKeyDictionary[Future, Pool[W]]" = __WeakKeyDictionary()

    __signaled = Event()
    __signaled_queue : "__deque[__ref[Pool[W]] | __ref[MapIterator] | Pool[W] | MapIterator]" = __deque()
    __signal_lock = Lock()

    @staticmethod
    def _signal(object : "Pool[W] | MapIterator", weak : bool = True):
        with Pool.__signal_lock:
            if weak and not Pool.__signaled_queue or not any(((s() is object) if isinstance(s, Pool.__ref) else (s is object)) for s in Pool.__signaled_queue):        # Useless to signal twice
                Pool.__logger.debug(f"Signaling {object} to Pool Scheduler")
                Pool.__signaled_queue.append(Pool.__ref(object)) # type: ignore
                Pool.__signaled.set()
            elif not weak:
                Pool.__logger.info(f"Strongly signaling {object} to Pool Scheduler")
                Pool.__signaled_queue.append(object)
                Pool.__signaled.set()
        


    class MapIterator(Generic[R]):

        """
        A parallel version of builtin map.
        """

        from sys import getsizeof as __getsizeof_init
        __getsizeof = staticmethod(__getsizeof_init)
        del __getsizeof_init
        from ..exceptions import FutureSetError as __FutureSetError
        from ...parallel import logger as __logger
        from weakref import ref as __ref, WeakKeyDictionary, WeakSet as __WeakSet
        from threading import RLock as __RLock, Event as __Event
        from collections import deque as __deque

        __ref_holder : "WeakKeyDictionary[Future[R], Pool.MapIterator]" = WeakKeyDictionary()
        del WeakKeyDictionary

        def __init__(self, pool : "Pool", pool_lock : "Pool.__PLock", func : Callable, iter : Iterator[tuple], cachesize : int | None = None, cachelen : int | None = None) -> None:
            self.__logger.debug(f"Initializing {self}")
            self.__pool = pool
            self.__pool_lock = pool_lock
            self.__func = func
            self.__iter = iter
            self.__cachesize = cachesize
            self.__cachelen = cachelen
            self.__queue : "deque[Future[R]]" = self.__deque()
            self.__queue_not_empty = self.__Event()
            self.__results_size : "dict[Future[R], int]" = {}
            self.__results_len = 0
            self.__active : "Pool.MapIterator.__WeakSet[Future[R]]" = Pool.MapIterator.__WeakSet()
            self.__lock = self.__RLock()
            self.__exhausted = False
            self.__deleted = False
            self.__deleting = False

        @property
        def pool(self) -> "Pool":
            """
            Returns the Pool that this MapIterator is attached to.
            """
            return self.__pool

        # Note that there are many static methods here to avoid holding references to MapIterator objects, allowing them to be deleted when they are no longer used, freeing the CPU...

        def __has_cache_space(self) -> bool:
            """
            Internal function used to check if the result cache has enough space to keep submitting tasks to the pool.
            """
            with self.__lock:
                if self.__cachesize is not None:
                    ok1 = sum(self.__results_size.values()) < self.__cachesize
                else:
                    ok1 = True
                if self.__cachelen is not None:
                    ok2 = self.__cachelen < self.__results_len
                else:
                    ok2 = True
                return ok1 and ok2
            
        @property
        def __notify(self) -> DefaultCallback:
            """
            Notifies the Pool scheduler to check the state of this MapIterator.
            It is actually a weak method property used to create a weak callback function (one that does not hold a reference to the instance).
            """
            rself: "ref[Pool.MapIterator[R]]" = self.__ref(self)
            del self

            def notify(fut : "Future[R] | None" = None):
                self = rself()
                if self is not None:
                    if not self.__pool.closed:
                        with self.__lock:
                            if fut is not None:
                                if fut in Pool.MapIterator.__ref_holder:
                                    Pool.MapIterator.__ref_holder.pop(fut)
                                self.__active.discard(fut)
                                if fut in self.__queue:
                                    self.__results_len += 1
                                    self.__results_size[fut] = self.__getsizeof(fut.value)
                        if not self.__exhausted:
                            Pool._signal(self)
                    else:
                        if fut is not None:
                            if fut in Pool.MapIterator.__ref_holder:
                                Pool.MapIterator.__ref_holder.pop(fut)
                            self.__active.discard(fut)
                            self.__queue_not_empty.set()
                
            return notify

        def _adjust_active_tasks(self):
            """
            Internal function used to declare tasks to the pool if some can be declared.
            """
            with self.__lock:
                if self.__deleting:
                    self.__close_mapiterator()
                    return
                if self.__pool.closed:
                    self.__exhausted = True
                    self.__queue_not_empty.set()
                    return
                if not self.__has_cache_space():
                    return
                while len(self.__active) < 2 * self.__pool.size or not self.__queue:
                    try:
                        next_args = next(self.__iter)
                        self.__queue.append(fut := self.__pool.apply_async(self.__func, *next_args))
                    except (StopIteration, RuntimeError):
                        self.__exhausted = True
                        self.__queue_not_empty.set()
                        return
                    fut.cancel_on_del = True
                    self.__queue_not_empty.set()
                    self.__active.add(fut)
                    fut.add_callback(self.__notify)

        def __iter__(self) -> Iterator[Future[R]]:
            """
            Implements iter(self).
            """
            return self
        
        def __next__(self) -> Future[R]:
            """
            Implements next(self).
            """
            with self.__lock:
                if not self.__queue:
                    if self.__exhausted:
                        raise StopIteration
                    self.__queue_not_empty.clear()
                    self.__notify()

            self.__queue_not_empty.wait()

            with self.__lock:
                try:
                    fut = self.__queue.popleft()
                except IndexError:
                    self.__logger.debug(f"{self} is exhausted")
                    raise StopIteration from None
                if fut in self.__results_size:
                    self.__results_size.pop(fut)
                    self.__results_len -= 1
                # This is to make sure that until futures that depend on this MapIterator still exist, this MapIterator will not get deleted.
                Pool.MapIterator.__ref_holder[fut] = self
                return fut
            
        def __del__(self):
            """
            Implements del self.
            """
            self.__logger.debug(f"Deleting {self}")
            with self.__lock:
                if self.__deleting:
                    return
                global closing
                closing = True
                self.__deleting = True
                self.__exhausted = True
                self.__queue.clear()
                self.__queue_not_empty.set()
            Pool._signal(self, weak=False)

        def __close_mapiterator(self):
            """
            Internal function used to cancel the Futures awaiting from this MapIterator.
            Note that it might not get called if all the Futures have already been cancelled and the object has successfully been destroyed.
            """
            excs : list[BaseException] = []
            with self.__lock, self.__pool_lock:
                self.__logger.info(f"Cleaning resources of {self}: got {len(self.__active)} Futures to cancel")
                if self.__deleted:
                    return
                for fut in self.__active.copy():
                    try:
                        fut.cancel()
                    except* self.__FutureSetError:
                        pass
                    except* BaseException as e:
                        excs.append(e)
                self.__deleted = True
            self.__logger.info(f"Cleaned up {self}")
            if excs:
                raise BaseExceptionGroup("Some errors occured while cancelling tasks", excs)
            


    
    class UnorderedMapIterator(Generic[R]):

        """
        Wrapper for MapIterators that will yield futures to the first result available of the iterator.
        """

        from threading import RLock as __RLock, Event as __Event
        from collections import deque as __deque
        from weakref import ref as __ref, WeakKeyDictionary, WeakSet
        from ..exceptions import FutureSetError as __FutureSetError, CancelledFuture as __CancelledFuture
        from ...parallel import logger as __logger
        __Future = None

        __ref_holder : "WeakKeyDictionary[Future[R], Pool.UnorderedMapIterator]" = WeakKeyDictionary()
        del WeakKeyDictionary

        def __init__(self, map_it : "Pool.MapIterator[R]", pool : "Pool[W]") -> None:
            self.__logger.debug(f"Initializing {self}")
            self.__map_it = map_it
            self.__lock = Pool.UnorderedMapIterator.__RLock()
            self.__pool = pool
            self.__active : "set[Future[R]]" = set()
            self.__future_queue : "Pool.__deque[ref[Future[R]]]" = Pool.UnorderedMapIterator.__deque()
            self.__result_queue : "Pool.__deque[Future[R]]" = Pool.UnorderedMapIterator.__deque()
            self.__result_event = Pool.UnorderedMapIterator.__Event()
            self.__index = 0
            if Pool.UnorderedMapIterator.__Future is None:
                from ..thread import Future
                Pool.UnorderedMapIterator.__Future = Future
            self.__notify()

        @property
        def pool(self) -> "Pool[W]":
            return self.__pool

        @property
        def __notify(self) -> DefaultCallback:
            """
            Creates a notifier for the UMap to ensure the next futures.
            """
            rself : "ref[Pool.UnorderedMapIterator[R]]" = self.__ref(self)
            rpool : "ref[Pool[W]]" = self.__ref(self.__pool) # type: ignore
            riter : "ref[Pool.MapIterator[R]]" = self.__ref(self.__map_it)
            del self

            def notify(fut : "Future | None" = None):
                pool = rpool()
                self = rself()
                map_it = riter()
                if fut is not None and fut in Pool.UnorderedMapIterator.__ref_holder:
                    Pool.UnorderedMapIterator.__ref_holder.pop(fut)
                if pool is not None and self is not None and map_it is not None:
                    with self.__lock:
                        if pool.closed:
                            self.__result_event.set()
                        if fut:
                            self.__active.discard(fut)
                        while len(self.__active) < pool.size or not self.__result_queue:
                            try:
                                nfut = next(map_it)
                            except StopIteration:
                                self.__result_event.set()
                                break
                            next_future = Pool.UnorderedMapIterator.__Future()       # type: ignore because it is set in __init__
                            self.__index += 1
                            next_future.name = f"UMap Iterator Future #{self.__index}"
                            self.__future_queue.append(Pool.UnorderedMapIterator.__ref(next_future))
                            self.__result_queue.append(next_future)
                            self.__result_event.set()
                            self.__active.add(nfut)
                            nfut.add_callback(self.__notify)
                            del nfut
                        if fut:
                            current_future = self.__future_queue.popleft()()
                            if current_future:
                                self.__logger.debug(f"Linking result {fut} to sorted result {current_future}")
                                try:
                                    fut.link(current_future)
                                except Pool.UnorderedMapIterator.__FutureSetError:
                                    if not current_future.is_set or current_future.exception is None or not isinstance(current_future.exception, Pool.UnorderedMapIterator.__CancelledFuture):
                                        raise Pool.UnorderedMapIterator.__FutureSetError("Future given by umap_async was set by user")

            return notify
        
        def __iter__(self) -> Iterator[Future[R]]:
            """
            Implements iter(self).
            """
            return self

        def __next__(self) -> Future[R]:
            """
            Implements next(self).
            """
            if not self.__result_queue:
                self.__notify()
            self.__result_event.wait()
            if not self.__result_queue:
                raise StopIteration
            with self.__lock:
                fut = self.__result_queue.popleft()
                if not self.__result_queue:
                    self.__result_event.clear()
                Pool.UnorderedMapIterator.__ref_holder[fut] = self
                return fut
            
        def __del__(self):
            self.__logger.debug(f"Deleting {self}")



    def __init__(self, maxsize : int, *, lazy : bool = True, max_tasks_per_child : int | float = float("inf")) -> None:
        if not isinstance(maxsize, int):
            raise TypeError(f"Expected int, got '{type(maxsize).__name__}'")
        if not isinstance(lazy, bool):
            raise TypeError(f"Expected bool for lazy, got '{type(lazy).__name__}'")
        if not isinstance(max_tasks_per_child, int | float):
            raise TypeError(f"Expected int or float for max_tasks_per_child, got '{type(max_tasks_per_child).__name__}'")
        if max_tasks_per_child != float("inf"):
            try:
                max_tasks_per_child = int(max_tasks_per_child)
            except:
                raise ValueError(f"Expected positive nonzero interger or float('inf') for max_tasks_per_child, got {max_tasks_per_child}")
        if max_tasks_per_child <= 0:
            raise ValueError(f"Expected positive nonzero interger or float('inf') for max_tasks_per_child, got {max_tasks_per_child}")
        if maxsize <= 0:
            raise ValueError(f"Expected positive nonzero size, got {maxsize}")
        self.__lazy = lazy
        self.__pool : "list[W]" = []
        self.__lock = self.__PLock()
        self.__affectations : "Pool.__WeakKeyDictionary[Future, W]" = Pool.__WeakKeyDictionary()
        self.__pending : "deque[tuple[Future, Callable, tuple, dict]]" = self.__deque()
        self.__maxsize = maxsize
        self.__closed : bool = False
        self.__index = 0
        self.__max_tasks_per_child = max_tasks_per_child
        self.__logger.debug(f"Initializing {self}")
        if not self.__lazy:
            self.__notify()

    __pool_scheduler_lock = Lock()

    @staticmethod
    def __pool_scheduler():
        """
        Internal function used to schedule the tasks of all the Pools!
        """
        from sys import getrefcount
        module_ready.wait()
        with Pool.__pool_scheduler_lock:
            pool_manager_ready.set()
            
            del Pool.__pool_scheduler         # Just to ensure it won't be lauched twice!

            Pool.__logger.info("Pool Scheduler starting!")

            while True:

                Pool.__signaled.wait()
                with Pool.__signal_lock:
                    rself = Pool.__signaled_queue.popleft()
                    if not Pool.__signaled_queue:
                        Pool.__signaled.clear()
                assert rself != None, f"Pool scheduler has not received a reference to an object to handle: received a '{type(rself).__name__}'"

                if isinstance(rself, Pool.__ref):
                    self = rself() # type: ignore
                else:
                    self = rself
                del rself

                Pool.__logger.debug(f"Pool Scheduler handling {self}")

                if isinstance(self, Pool):
                    with self.__lock:
                        if not self.__closed:
                            self.__cleanup_pool()
                            if not self.__adjust_pool():
                                while self.__pending and len(self.__affectations) < self.size:
                                    fut, func, args, kwargs = self.__pending.popleft()
                                    if getrefcount(fut) < 3:        # This means that no one is waiting for this future...skip it.
                                        del fut
                                        continue
                                    if not fut.cancelled:
                                        chosen_worker = None
                                        for w in self.__pool:
                                            if w not in self.__affectations.values():
                                                if not w.busy:
                                                    chosen_worker = w
                                                    break
                                        if chosen_worker is None:       # Happens with very bad luck in the garbage collection cycle...
                                            self.__pending.appendleft((fut, func, args, kwargs))
                                            self.__notify()         # Just try again...
                                            del fut
                                            break
                                        self.__index += 1
                                        fut.name = f"Pool Future for task #{self.__index}"
                                        fut.cancel_on_del = True
                                        self.__affectations[fut] = chosen_worker
                                        fut.add_callback(self.__notify)
                                        Pool.__logger.debug(f"Affecting {fut} to {chosen_worker}")
                                        imediate_fut = chosen_worker.execute_async(func, *args, **kwargs)
                                        imediate_fut.name = f"Worker Future for task #{self.__index}"
                                        imediate_fut.link(fut)
                                        del imediate_fut
                                    del fut
                        
                        else:
                            self.__close_pool()
                
                elif isinstance(self, Pool.MapIterator):
                    self._adjust_active_tasks()

                elif self is None:
                    pass
                
                else:
                    raise RuntimeError(f"Pool scheduler has been signaled to handle a non-Pool related object : received a reference to a '{type(self).__name__}'")
                
                del self

    __DaemonThread(target = __pool_scheduler, name = "Pool Scheduler Thread").start()

    @property
    def __notify(self) -> DefaultCallback:
        """
        Notifies the Pool scheduler to check the state of this Pool.
        It is actually a weak method property used to create a weak callback function (one that does not hold a reference to the instance).
        """
        rself: "ref[Pool[W]]" = self.__ref(self)
        del self

        def notify(fut : "Future | None" = None):
            self = rself()
            if self is not None:
                Pool.__logger.debug(f"{fut} set, notifying {self}")
                if fut is not None and fut in Pool.__ref_holder:
                    Pool.__ref_holder.pop(fut)
                Pool._signal(self)
            
        return notify
    
    def __cleanup_pool(self):
        """
        Internal function used to free workers who have finished their tasks.
        """
        with self.__lock:
            for fut in self.__affectations.copy():
                if fut.is_set:
                    w = self.__affectations.pop(fut)
                    if w.busy:
                        Pool.__logger.info(f"{fut} cancelled: killing {self}'s worker '{w}'")
                        w.kill()
                        self.__pool.remove(w)
                    elif w.task_count >= self.__max_tasks_per_child:
                        Pool.__logger.info(f"{fut} set and worker {w} is exhausted: killing {self}'s worker '{w}'")
                        w.kill()
                        self.__pool.remove(w)

    def __close_pool(self):
        """
        Internal function used to cancel the Futures and kill the workers when closing.
        """
        with self.__lock:
            Pool.__logger.info(f"Cleaning up {self}: got {len(self.__pending)} pending and {len(self.__affectations)} affected Futures to cancel")
            excs : list[BaseException] = []
            for fut, func, args, kwargs in self.__pending:
                try:
                    fut.cancel()
                except* self.__FutureSetError:
                    pass
                except* BaseException as e:
                    excs.append(e)
            self.__pending.clear()
            for fut in self.__affectations:
                try:
                    fut.cancel()
                except* self.__FutureSetError:
                    pass
                except* BaseException as e:
                    excs.append(e)
            self.__affectations.clear()
            for w in self.__pool:
                try:
                    w.kill()
                except:
                    pass
            self.__pool.clear()
            if excs:
                raise BaseExceptionGroup("Some errors occured while cancelling tasks", excs)

    def __add_worker(self):
        """
        Internal function used to create a new worker in the background.
        """
        if not self.__closed:
            Pool.__logger.debug("Spawning new worker")
            self.__pool.append(self._spawn())

    def __remove_worker(self, worker : W):
        """
        Internal function used to remove a worker in the background.
        """
        Pool.__logger.debug("Killing worker")
        self.__pool.remove(worker)
        worker.kill()
    
    def __adjust_pool(self) -> bool:
        """
        Internal function to spawn missing workers.
        Returns True if there are pending operations on the Pool after the call to this method.
        """
        tasks_pending = False
        with self.__lock:
            if self.__closed:
                missing = len(self.__pool) - len(self.__affectations)
            else:
                missing = self.size - len(self.__pool)
                if self.__lazy:
                    missing = min(missing, max(0, len(self.__pending) - (len(self.__pool) - len(self.__affectations))))
            if missing > 0 and not self.__closed:
                Pool.__logger.info(f"Adding {missing} Workers for {self}")
                threads = [self.__DaemonThread(target = self.__add_worker, name = f"Worker Spawner #{n}") for n in range(missing)]
                def waiter_1():
                    with self.__lock:
                        for t in threads:
                            t.start()
                        for t in threads:
                            t.join()
                    self.__notify()
                w = self.__DaemonThread(target = waiter_1, name = "Pool Adjuster Notifier")
                self.__lock.pass_on(w)
                w.start()
                tasks_pending = True
            elif missing < 0:
                excess = -missing
                Pool.__logger.info(f"Removing {excess} Workers from {self}")
                removed = 0
                to_remove : "list[W]" = []
                for w in self.__pool:
                    if w not in self.__affectations.values():
                        to_remove.append(w)
                        removed += 1
                    if removed >= excess:
                        break
                threads = [self.__DaemonThread(target = self.__remove_worker, args = (w, ), name = f"Worker Spawner #{n}") for n, w in enumerate(to_remove)]
                def waiter_2():
                    with self.__lock:
                        for t in threads:
                            t.start()
                        for t in threads:
                            t.join()
                    self.__notify()
                w = self.__DaemonThread(target = waiter_2, name = "Pool Adjuster Notifier")
                self.__lock.pass_on(w)
                w.start()
                tasks_pending = True
            return tasks_pending

    @property
    def size(self) -> int:
        """
        The maximum number of workers that can be in the Pool.
        """
        return self.__maxsize
    
    @size.setter
    def size(self, maxsize : int):
        """
        Sets the size of the pool, starting new workers if possible and tasks are pending.
        Note that reducing the size of the pool might be postponed if all workers are active (just enough will die when they complete their active task).
        """
        if not isinstance(maxsize, int):
            raise TypeError(f"Expected int, got '{type(maxsize).__name__}'")
        if maxsize <= 0:
            raise ValueError(f"Expected positive nonzero size, got {maxsize}")
        with self.__lock:
            if self.__closed:
                raise RuntimeError("Pool is closing")
        self.__maxsize = maxsize
        self.__notify()
        
    def close(self):
        """
        Closes the Pool. Not more task can be submitted. Also kills all the active workers.
        """
        with self.__lock:
            if self.__closed:
                return
            Pool.__logger.debug(f"Closing {self}")
            self.__closed = True
        Pool._signal(self, weak = False)
    
    @property
    def closed(self) -> bool:
        """
        Indicates if the bool has been closed.
        """
        return self.__closed
    
    @closed.setter
    def closed(self, value : bool):
        if not isinstance(value, bool):
            raise TypeError(f"Expected bool, got '{type(value).__name__}'")
        if self.__closed and not value:
            raise ValueError("Cannot re-open a Pool")
        if value:
            self.close()
    
    @classmethod
    @abstractmethod
    def _spawn(cls) -> W:
        """
        Creates a Worker object. Used internally to maintain the worker pool.
        """
        raise NotImplementedError(f"You need to implement the '_spawn' method of the '{cls.__name__}' class")
        
    def __del__(self):
        """
        Implements del self. 
        """
        self.close()

    def __enter__(self):
        """
        Implements with self:
        """
        if not self.__lazy:
            self.__notify()
        return self
    
    def __exit__(self, exc_type : type[BaseException], exc : BaseException, tb : TracebackType):
        """
        Implements with self:
        """
        self.close()

    def is_running(self, f : Future) -> bool:
        """
        Returns True if the given Future matches a task that is currently being executed by the pool.
        """
        if not isinstance(f, Future):
            raise TypeError(f"Expected Future, got '{type(f).__name__}'")
        return f in self.__affectations
    
    def is_pending(self, f : Future) -> bool:
        """
        Returns True if the given Future matches a task that is currently waiting in the pool queue.
        """
        if not isinstance(f, Future):
            raise TypeError(f"Expected Future, got '{type(f).__name__}'")
        with self.__lock:
            return f in (fut for fut, func, args, kwargs in self.__pending)
    
    def apply_async(self, func : Callable[P, R], *args : P.args, **kwargs : P.kwargs) -> Future[R]:
        """
        Starts the execution of the function func with given arguments in the first available worker.
        Returns Task object to control the execution of the task.
        """
        if self.__closed:
            raise RuntimeError("Pool is closed")
        from ..thread.future import Future
        with self.__lock:
            t : "Future[R]" = Future()
            t.name = "Unscheduled Pool Future"
            Pool.__ref_holder[t] = self
            Pool.__logger.debug(f"Declaring new task in {self}: {(t, func, args, kwargs)}")
            self.__pending.append((t, func, args, kwargs))
            self.__notify()
        return t
        
    def apply(self, func : Callable[P, R], *args : P.args, **kwargs : P.kwargs) -> R:
        """
        Starts the execution of the function func with given arguments in the first available worker and returns the result.
        """
        return self.apply_async(func, *args, **kwargs).result()
    
    # Don't be scared, we are just making valid type annotations up until 10-arguments functions...Because Python typing is great :)
    
    T0, T1, T2, T3, T4, T5, T6, T7, T8, T9 = TypeVar("T0"), TypeVar("T1"), TypeVar("T2"), TypeVar("T3"), TypeVar("T4"), TypeVar("T5"), TypeVar("T6"), TypeVar("T7"), TypeVar("T8"), TypeVar("T9")

    @overload
    def map_async(self, func : Callable[[T0], R], iterable_0 : Iterable[T0], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4, T5], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...
    @overload
    def map_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], iterable_9 : Iterable[T9], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]:
            ...

    def map_async(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> MapIterator[R]: # type: ignore since variadic generic are not yet supported...
        """
        Parallel asynchronous version of map. The returned iterator will yield the awaitable results computed by the Pool.
        Note that results from the iterator will be computed in advance.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        from typing import Iterable
        if not callable(func):
            raise TypeError(f"Expected callable, got '{type(func).__name__}'")
        for it in iterables:
            if not isinstance(it, Iterable):
                raise TypeError(f"Expected callable and iterables, got a '{type(it).__name__}'")
        if not isinstance(cachesize, int) and not (isinstance(cachesize, float) and cachesize == float("inf")):
            raise TypeError(f"Expected int or float(\"inf\") for cachesize, got '{type(cachesize).__name__}'")
        if cachesize <= 0:
            raise ValueError(f"Expected positive nonzero integer for cachesize, got {cachesize}")
        if not isinstance(cachelen, int) and not (isinstance(cachelen, float) and cachelen == float("inf")):
            raise TypeError(f"Expected int or float(\"inf\") for cachelen, got '{type(cachelen).__name__}'")
        if cachelen <= 0:
            raise ValueError(f"Expected positive nonzero integer for cachelen, got {cachelen}")
        return self.MapIterator(self, self.__lock, func, zip(*iterables), cachesize if not isinstance(cachesize, float) else None, cachelen if not isinstance(cachelen, float) else None)
        
    @overload
    def map(self, func : Callable[[T0], R], iterable_0 : Iterable[T0], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4, T5], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def map(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], iterable_9 : Iterable[T9], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...

    def map(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:    # type: ignore since variadic generic are not yet supported...
        """
        Parallel version of map. The returned iterator will yield the results computed by the Pool.
        Note that results from the iterator will be computed in advance.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        return (r.result() for r in self.map_async(func, *iterables, cachesize=cachesize, cachelen=cachelen))
    
    @overload
    def umap_async(self, func : Callable[[T0], R], iterable_0 : Iterable[T0], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:   
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4, T5], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...
    @overload
    def umap_async(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], iterable_9 : Iterable[T9], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:
            ...

    def umap_async(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> UnorderedMapIterator[R]:  # type: ignore since variadic generic are not yet supported...
        """
        Parallel asynchronous unordered version of map. The returned iterator will yield futures to the first results available computed by the Pool.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        return Pool.UnorderedMapIterator(self.map_async(func, *iterables, cachesize=cachesize, cachelen=cachelen), self)

    @overload
    def umap(self, func : Callable[[T0], R], iterable_0 : Iterable[T0], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:        
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4, T5], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...
    @overload
    def umap(self, func : Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], R], iterable_0 : Iterable[T0], iterable_1 : Iterable[T1], iterable_2 : Iterable[T2], iterable_3 : Iterable[T3], iterable_4 : Iterable[T4], iterable_5 : Iterable[T5], iterable_6 : Iterable[T6], iterable_7 : Iterable[T7], iterable_8 : Iterable[T8], iterable_9 : Iterable[T9], *, cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:
            ...

    def umap(self, func : Callable[[*tuple[T]], R], *iterables : Iterable[T], cachesize : int | float = float("inf"), cachelen : int | float = float("inf")) -> Generator[R, None, None]:   # type: ignore since variadic generic are not yet supported...
        """
        Parallel unordered version of map. The returned iterator will yield the first results available computed by the Pool.
        "cachesize" limits the memory size of stored results.
        "cachelen" limits the number of results that should be stored.
        """
        yield from (r.result() for r in self.umap_async(func, *iterables, cachesize=cachesize, cachelen=cachelen))

    del T0, T1, T2, T3, T4, T5, T6, T7, T8, T9





module_ready.set()
pool_manager_ready.wait()
del module_ready, pool_manager_ready





del P, R, Y, S, T, W, ABCMeta, abstractmethod, deque, Event, Lock, TracebackType, Callable, Generator, Generic, Iterable, Iterator, ParamSpec, Protocol, TypeVar, overload, ref, Future