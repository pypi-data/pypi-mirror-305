"""
This module is used for creating multiple signal handlers from any threads.

Use add_handler(handler : HandlerType, *sig : Signals) and remove_handler(handler : HandlerType, *sig : Signals) to register/unregister signal handlers.
This is done using the Enum Signals:
>>> add_handler(handler, Signals.SIGBREAK, Signals.SIGINT)

You can also manage handlers from the Signals:
>>> Signals.SIGINT.add_handler(handler)

Note that this is build over the signal module. Using signal.signal() after loading this module will cause the corresponding handlers to be missed.
Also note that handlers will be called in the order in which they were added.
"""

import signal, sys
from types import FrameType
from typing import Callable
from enum import IntEnum

__all__ = ["add_handler", "remove_handler", "handlers", "clear_handlers", "Signal"]





from threading import current_thread, main_thread
if current_thread() != main_thread():
    raise RuntimeError("The Boa.signal module should be loaded by the main thread")
del current_thread, main_thread





if sys.platform == "win32":

    class Signal(IntEnum):

        """
        A class that holds all the signals that can be received and allows the manage their handlers.
        """

        SIGINT = signal.SIGINT
        "Interrupt"
        SIGILL = signal.SIGILL
        "Illegal instruction"
        SIGFPE = signal.SIGFPE
        "Floating point exception"
        SIGSEGV = signal.SIGSEGV
        "Segmentation fault"
        SIGTERM = signal.SIGTERM
        "Terminated"
        SIGBREAK = signal.SIGBREAK
        "Keyboard Interrupt"
        SIGABRT = signal.SIGABRT
        "Aborted"

        def __new__(cls, value : int):
            from signal import valid_signals
            signals = {s.value : s for s in valid_signals() if hasattr(s, "value") and hasattr(s, "name")}
            try:
                sig = signals[value]
            except:
                raise ValueError(f"Unknown signal: {value}")
            try:
                sig.name
            except:
                raise ValueError(f"Unnamed signal: {value}")
            return int.__new__(cls, value)      # I don't know...EnumTypes...

        def __init__(self, value : int) -> None:
            from collections import OrderedDict
            from signal import strsignal, valid_signals, signal
            from threading import RLock
            self.__lock = RLock()
            self.__value = value
            signals = {s.value : s for s in valid_signals() if hasattr(s, "value") and hasattr(s, "name")}
            try:
                sig = signals[value]
            except:
                raise ValueError(f"Unknown signal: {value}")
            try:
                self.__name = sig.name
            except:
                raise ValueError(f"Unnamed signal: {value}")
            try:
                self.__doc = strsignal(value) or "Unknown"
            except:
                self.__doc = "Unknown"
            self.__hookable = True
            try:
                signal(value, self.__handler)
            except:
                self.__hookable = False
            self.__handlers : OrderedDict[Callable[["Signal"], None], bool] = OrderedDict()

        @property
        def name(self) -> str:
            """
            The signal name. Use Signal.<name> to get this same signal object.
            """
            return self.__name
        
        @property
        def value(self) -> int:
            """
            The signal integer value.
            """
            return self.__value
        
        @property
        def doc(self) -> str:
            """
            A small docstring that describes what this signal does.
            """
            return self.__doc
        
        @property
        def hookable(self) -> bool:
            """
            Indicates if handlers can be hooked to this signal.
            """
            return self.__hookable
        
        def add_handler(self, handler : Callable[["Signal"], None], *, add_note_on_exception : bool = True):
            """
            Adds another handler for this signal.
            If add_note_on_exception is True and an error occurs in the handler, a note indicating the signal will be added to the exception.
            """
            if not callable(handler):
                raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
            if not isinstance(add_note_on_exception, bool):
                raise TypeError(f"Exepcted bool for add_note_on_exception, got '{type(add_note_on_exception).__name__}'")
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                self.__handlers[handler] = add_note_on_exception

        def remove_handler(self, handler : Callable[["Signal"], None]):
            """
            Removes the given handler for this signal.
            """
            if not callable(handler):
                raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                if handler not in self.__handlers:
                    raise ValueError("Handler has never been hooked to that signal")
                self.__handlers.pop(handler)

        def clear_handlers(self):
            """
            Removes all the handlers for this signal.
            """
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                self.__handlers.clear()

        @property
        def handlers(self) -> tuple[Callable[["Signal"], None], ...]:
            """
            Returns the sequence of handlers for this signal in the order in which they should be called.
            """
            return tuple(self.__handlers)
        
        def __handler(self, signal : int, frame : FrameType | None):
            """
            The internal signal handler.
            """
            with self.__lock:
                for handler, add_note in self.__handlers.items():
                    try:
                        handler(self)
                    except BaseException as e:
                        if add_note:
                            e.add_note(f"Exception occured after receiving signal {self.name} and calling {handler.__name__}(Signal.{self.name}).")
                        if e.__traceback__ is not None:
                            e.__traceback__ = e.__traceback__.tb_next
                        raise




else:
        
    class Signal(IntEnum):

        """
        A class that holds all the signals that can be received and allows the manage their handlers.
        """

        SIGHUP = signal.SIGHUP
        "Hangup"
        SIGINT = signal.SIGINT
        "Interrupt"
        SIGILL = signal.SIGILL
        "Illegal instruction"
        SIGABRT = signal.SIGABRT
        "Aborted"
        SIGBUS = signal.SIGBUS
        "Bus error"
        SIGFPE = signal.SIGFPE
        "Floating point exception"
        SIGKILL = signal.SIGKILL
        "Killed"
        SIGUSR1 = signal.SIGUSR1
        "User defined signal 1"
        SIGSEGV = signal.SIGSEGV
        "Segmentation fault"
        SIGUSR2 = signal.SIGUSR2
        "User defined signal 2"
        SIGPIPE = signal.SIGPIPE
        "Broken pipe"
        SIGALRM = signal.SIGALRM
        "Alarm clock"
        SIGTERM = signal.SIGTERM
        "Terminated"
        SIGSTKFLT = signal.SIGSTKFLT
        "Stack fault"
        SIGCHLD = signal.SIGCHLD
        "Child exited"
        SIGCONT = signal.SIGCONT
        "Continued"
        SIGWINCH = signal.SIGWINCH
        "Window changed"

        def __new__(cls, value : int):
            from signal import valid_signals
            signals = {s.value : s for s in valid_signals() if hasattr(s, "value") and hasattr(s, "name")}
            try:
                sig = signals[value]
            except:
                raise ValueError(f"Unknown signal: {value}")
            try:
                sig.name
            except:
                raise ValueError(f"Unnamed signal: {value}")
            return int.__new__(cls, value)      # I don't know...EnumTypes...

        def __init__(self, value : int) -> None:
            from collections import OrderedDict
            from signal import strsignal, valid_signals, signal
            from threading import RLock
            self.__lock = RLock()
            self.__value = value
            signals = {s.value : s for s in valid_signals() if hasattr(s, "value") and hasattr(s, "name")}
            try:
                sig = signals[value]
            except:
                raise ValueError(f"Unknown signal: {value}")
            try:
                self.__name = sig.name
            except:
                raise ValueError(f"Unnamed signal: {value}")
            try:
                self.__doc = strsignal(value) or "Unknown"
            except:
                self.__doc = "Unknown"
            self.__hookable = True
            try:
                signal(value, self.__handler)
            except:
                self.__hookable = False
            self.__handlers : OrderedDict[Callable[["Signal"], None], bool] = OrderedDict()

        @property
        def name(self) -> str:
            """
            The signal name. Use Signal.<name> to get this same signal object.
            """
            return self.__name
        
        @property
        def value(self) -> int:
            """
            The signal integer value.
            """
            return self.__value
        
        @property
        def doc(self) -> str:
            """
            A small docstring that describes what this signal does.
            """
            return self.__doc
        
        @property
        def hookable(self) -> bool:
            """
            Indicates if handlers can be hooked to this signal.
            """
            return self.__hookable
        
        def add_handler(self, handler : Callable[["Signal"], None], *, add_note_on_exception : bool = True):
            """
            Adds another handler for this signal.
            If add_note_on_exception is True and an error occurs in the handler, a note indicating the signal will be added to the exception.
            """
            if not callable(handler):
                raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
            if not isinstance(add_note_on_exception, bool):
                raise TypeError(f"Exepcted bool for add_note_on_exception, got '{type(add_note_on_exception).__name__}'")
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                self.__handlers[handler] = add_note_on_exception

        def remove_handler(self, handler : Callable[["Signal"], None]):
            """
            Removes the given handler for this signal.
            """
            if not callable(handler):
                raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                if handler not in self.__handlers:
                    raise ValueError("Handler has never been hooked to that signal")
                self.__handlers.pop(handler)

        def clear_handlers(self):
            """
            Removes all the handlers for this signal.
            """
            if not self.hookable:
                raise ValueError(f"Signal {self.name} is not hookable")
            with self.__lock:
                self.__handlers.clear()

        @property
        def handlers(self) -> tuple[Callable[["Signal"], None], ...]:
            """
            Returns the sequence of handlers for this signal in the order in which they should be called.
            """
            return tuple(self.__handlers)
        
        def __handler(self, signal : int, frame : FrameType | None):
            """
            The internal signal handler.
            """
            with self.__lock:
                for handler, add_note in self.__handlers.items():
                    try:
                        handler(self)
                    except BaseException as e:
                        if add_note:
                            e.add_note(f"Exception occured after receiving signal {self.name} and calling {handler.__name__}(Signal.{self.name}).")
                        if e.__traceback__ is not None:
                            e.__traceback__ = e.__traceback__.tb_next
                        raise





def add_handler(handler : Callable[[Signal], None], *signals : Signal):
    """
    Adds signal handler to all given signals.
    """
    if not callable(handler):
        raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
    for s in signals:
        if not isinstance(s, Signal):
            raise TypeError(f"Expected Signal, got '{type(s).__name__}'")
    for s in signals:
        s.add_handler(handler)

def remove_handler(handler : Callable[[Signal], None], *signals : Signal):
    """
    Adds signal handler to all given signals.
    """
    if not callable(handler):
        raise TypeError(f"Expected callable, got '{type(handler).__name__}'")
    for s in signals:
        if not isinstance(s, Signal):
            raise TypeError(f"Expected Signal, got '{type(s).__name__}'")
    for s in signals:
        s.remove_handler(handler)

def handlers() -> dict[Signal, tuple[Callable[[Signal], None], ...]]:
    """
    Returns a dictionary of the sequence of handlers for each signal.
    """
    return {s : s.handlers for s in Signal}

def clear_handlers():
    """
    Removes all signal handlers.
    """
    for s in Signal:
        if s.hookable:
            s.clear_handlers()

def KeyboardInterruptHandler(sig : Signal):
    """
    Default SIGINT handler. Raises KeyboardInterrupt.
    """
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt as e:
        e.__traceback__ = e.__traceback__.tb_next # type: ignore I just raised it. It has exactly one.
        raise

Signal.SIGINT.add_handler(KeyboardInterruptHandler, add_note_on_exception=False)

if sys.platform == "win32":
    Signal.SIGBREAK.add_handler(KeyboardInterruptHandler, add_note_on_exception=False)





del signal, sys, FrameType, Callable, IntEnum