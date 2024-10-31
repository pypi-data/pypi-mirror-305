"""
This is the main code of Manager processes.
"""

import sys
from os import fdopen, urandom
from socket import create_server, socket
from pickle import dumps
from threading import RLock, Thread, Event
from hmac import digest, compare_digest
from Viper.pickle_utils import WhiteListUnpickler
from .resource_manager import SharedResource

w = int(sys.argv[1])
parent_pid = int(sys.argv[2])

if sys.platform == "win32":     # In the case of Windows, we receive a handle that only exists in the parent process. Duplicate it and create a file descriptor

    from msvcrt import open_osfhandle

    from _winapi import (DUPLICATE_SAME_ACCESS, PROCESS_DUP_HANDLE,
                        SYNCHRONIZE, DuplicateHandle, GetCurrentProcess,
                        OpenProcess)

    parent_process = OpenProcess(
        SYNCHRONIZE | PROCESS_DUP_HANDLE,
        False,
        parent_pid
    )

    pipe_handle = DuplicateHandle(
        parent_process,
        w,
        GetCurrentProcess(),
        0,
        False,
        DUPLICATE_SAME_ACCESS | SYNCHRONIZE
        )
    
    w = open_osfhandle(pipe_handle, 0)    

server_socket = create_server(("localhost", 0))
key = urandom(64)

with fdopen(w, "wb") as from_parent:
    
    data = dumps(server_socket.getsockname())
    
    from_parent.write(len(data).to_bytes(8, "little"))
    from_parent.write(data)
    from_parent.write(key)

connections : set[socket] = set()
work_table : dict[bytes, int] = {}
per_socket_work : dict[bytes, dict[socket, int]] = {}
resources : dict[bytes, type[SharedResource]] = {}
lock = RLock()


def increase(ident : bytes, sock : socket, cls : type[SharedResource]):
    with lock:
        if ident not in work_table:
            cls.__manager_init__(ident)
        work_table.setdefault(ident, 0)
        per_socket_work.setdefault(ident, {})
        resources[ident] = cls
        per_socket_work.setdefault(ident, {}).setdefault(sock, 0)
        work_table[ident] += 1
        per_socket_work[ident][sock] += 1

def decrease(ident : bytes, sock : socket):
    with lock:
        work_table[ident] -= 1
        per_socket_work[ident][sock] -= 1
        if not per_socket_work[ident][sock]:
            per_socket_work[ident].pop(sock)
            if not per_socket_work[ident]:
                per_socket_work.pop(ident)
        if not work_table[ident]:
            work_table.pop(ident)
            resources[ident].__manager_del__(ident)
            resources.pop(ident)

def clear_socket(sock : socket):
    with lock:
        for ident, references in per_socket_work.copy().items():
            if sock in references:
                for i in range(references[sock]):
                    decrease(ident, sock)





def handle_connection(s : socket, ready : Event):

    connections.add(s)
    ready.set()

    nonce = urandom(64)
    s.send(nonce)
    d = s.recv(64)
    if not compare_digest(d, digest(key, nonce, "sha512")):
        return
    nonce = s.recv(64)
    s.send(digest(key, nonce, "sha512"))

    try:
        while True:
            flag = int.from_bytes(s.recv(1), "little")
            match flag:

                case SharedResource.__ACTIONS__.INCREASE:
                    size = int.from_bytes(s.recv(8), "little")
                    ident = s.recv(size)
                    size = int.from_bytes(s.recv(8), "little")
                    unp = WhiteListUnpickler()
                    unp.allow_class_hierarchy(SharedResource)
                    unp << s.recv(size)
                    cls = unp.load()
                    increase(ident, s, cls)

                case SharedResource.__ACTIONS__.DECREASE:
                    size = int.from_bytes(s.recv(8), "little")
                    ident = s.recv(size)
                    decrease(ident, s)

                case b"":
                    break
        
    except ConnectionError:
        pass
    finally:
        clear_socket(s)
        connections.remove(s)


def start_server():

    sock, add = server_socket.accept()
    ready = Event()

    Thread(target = handle_connection, args = (sock, ready), name = f"Server for connection {add}").start()

    ready.wait()


def server():

    while connections:

        start_server()





start_server()
Thread(target = server, name = "Main Server", daemon = True).start()