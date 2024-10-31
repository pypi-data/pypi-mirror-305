"""
This module implements a resource server that ensures garbage collection at multiprocessing level.
"""

from abc import ABCMeta, abstractmethod
from subprocess import Popen
from typing import Any, Callable, Hashable
from enum import IntEnum
from pathlib import Path
import sys

__all__ = ["SharedResource", "ResourceManager", "main_manager"]





class SharedResource(metaclass = ABCMeta):

    """
    An abstract class for objects that are shared between different processes and need to be managed.
    To function properly, subclasses should call super().__init__() and super().__setstate__() before returning when overloading these methods.
    """

    __ACTIONS__ = IntEnum("ACTIONS", ("INCREASE", "DECREASE"))
    __RESOURCE_MANAGER__ : "ResourceManager"

    @abstractmethod
    def __manager_reduce__(self) -> bytes:
        """
        This function should return an identication bytestring that will be used by the manager to find the resource.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __manager_init__(ident : bytes):
        """
        This function is called by the manager to load the object to manage given the identication string returned by _manager_reduce().
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __manager_del__(ident : bytes):
        """
        This function is called by the manager to clean the object to manage given the identication string returned by _manager_reduce().
        """
        raise NotImplementedError
    
    def __init_subclass__(cls) -> None:
        if not hasattr(cls, "__RESOURCE_MANAGER__"):
            raise ValueError("SharedResource subclasses should define a '__RESOURCE_MANAGER__' class property")
        if not isinstance(cls.__RESOURCE_MANAGER__, ResourceManager):
            raise TypeError(f"SharedResource subclasses property '__RESOURCE_MANAGER__' should be a ResourceManager, got a '{type(cls.__RESOURCE_MANAGER__).__name__}'")
    
    def __init__(self) -> None:
        self.__RESOURCE_MANAGER__ = type(self).__RESOURCE_MANAGER__
        self.__RESOURCE_MANAGER__.increase_object(self)

    def __getstate__(self) -> dict[str, Any]:
        return {
            "__RESOURCE_MANAGER__" : self.__RESOURCE_MANAGER__
        }
    
    def __setstate__(self, state):
        self.__RESOURCE_MANAGER__ : "ResourceManager" = state["__RESOURCE_MANAGER__"]
        self.__RESOURCE_MANAGER__.increase_object(self)
    
    def __del__(self):
        self.__RESOURCE_MANAGER__.decrease_object(self)





class ResourceManager:

    """
    A subprocess that can be contacted to add or remove references to multiprocessing objects.
    """
    
    from threading import RLock as __RLock
    from Viper.pickle_utils import safe_loads
    from socket import create_connection
    from hmac import digest, compare_digest
    from os import urandom
    from multiprocessing import AuthenticationError as __AuthenticationError
    from pickle import dumps
    __create_connection = staticmethod(create_connection)
    __safe_loads = staticmethod(safe_loads)
    __digest = staticmethod(digest)
    __compare_digest = staticmethod(compare_digest)
    __urandom = staticmethod(urandom)
    __dumps = staticmethod(dumps)
    del create_connection, safe_loads, digest, compare_digest, urandom, dumps

    def __init__(self) -> None:
        self.__initialized : bool = False
        self.__lock = ResourceManager.__RLock()

    def __post_init__(self):
        with self.__lock:
            if self.__initialized:
                return
            self.__initialized = True

            r, close = self.__spawner()

            # For now, the bridge is not confidential :
            # anyone who has access to the underlying shared array will be able to read what was shared.

            with open(r, "rb", closefd=False) as pipe:

                data_size = int.from_bytes(pipe.read(8), "little")
                address = ResourceManager.__safe_loads(pipe.read(data_size))

                self.__key = pipe.read(64)
                self.__socket = ResourceManager.__create_connection(address)
            
            close()

            self.__authenticate()

    def __authenticate(self):
        """
        Internal function that handles authentication to the server process.
        """
        with self.__lock:
            nonce = self.__socket.recv(64)
            self.__socket.send(ResourceManager.__digest(self.__key, nonce, "sha512"))
            nonce = ResourceManager.__urandom(64)
            self.__socket.send(nonce)
            if not ResourceManager.__compare_digest(self.__socket.recv(64), ResourceManager.__digest(self.__key, nonce, "sha512")):
                raise ResourceManager.__AuthenticationError("Could not authenticate manager process")

    if sys.platform == "win32":

        # Yes on windows, you have to create the pipe "manually", because os.pipe() is useless...instead of fd, we use handles

        def __spawner(self) -> tuple[int, Callable[[], None]]:
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
            rfd = open_osfhandle(r, 0)
            Popen(args=[executable, "-m", "Boa.parallel.process.primitives.manager_process", str(w), str(getpid())], env=environ.copy())
            return rfd, lambda : CloseHandle(r) and CloseHandle(w)

    else:

        def __spawner(self) -> tuple[int, Callable[[], None]]:
            """
            Internal function to spawn the worker process.
            Returns a Popen object,  a file descriptor to a writing pipe to communicate with the child and a function to call to close the pipe.
            """
            from os import close, environ, getpid, pipe
            from subprocess import Popen
            from sys import executable
            r, w = pipe()
            Popen(args=[executable, "-m", "Boa.parallel.process.primitives.manager_process", str(w), str(getpid())], executable=executable, env=environ.copy(), pass_fds=[w])
            return r, lambda : close(r) and close(w)
    
    def __getstate__(self):
        self.__post_init__()
        return (self.__key, self.__socket.getpeername())
    
    def __setstate__(self, state : tuple[bytes, tuple[str, int]]):
        self.__initialized : bool = True
        self.__lock = ResourceManager.__RLock()
        with self.__lock:
            self.__key = state[0]
            self.__socket = ResourceManager.__create_connection(state[1])
            self.__authenticate()

    def increase_object(self, resource : SharedResource):
        """
        Increases the reference count of the resource in the manager.
        """
        with self.__lock:
            self.__post_init__()
            data = resource.__manager_reduce__()
            self.__socket.send(bytes([SharedResource.__ACTIONS__.INCREASE]))
            self.__socket.send(len(data).to_bytes(8, "little"))
            self.__socket.send(data)
            data = ResourceManager.__dumps(type(resource))
            self.__socket.send(len(data).to_bytes(8, "little"))
            self.__socket.send(data)

    def decrease_object(self, resource : SharedResource):
        """
        Decreases the reference count of the resource in the manager.
        """
        with self.__lock:
            self.__post_init__()
            data = resource.__manager_reduce__()
            self.__socket.send(bytes([SharedResource.__ACTIONS__.DECREASE]))
            self.__socket.send(len(data).to_bytes(8, "little"))
            self.__socket.send(data)





main_manager = ResourceManager()





del ABCMeta, abstractmethod, Popen, Any, Callable, Hashable, IntEnum, Path, sys