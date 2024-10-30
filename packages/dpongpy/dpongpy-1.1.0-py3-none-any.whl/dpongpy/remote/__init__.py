import socket
from typing import Protocol
from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class Address:
    host: str = field()
    port: int

    def __post_init__(self):
        self._ip = None
        if isinstance(self.port, str):
            self.port = int(self.port)
        assert 0 <= self.port <= 65535, "Port number must be between 0 and 65535"
        self.host = (self.host or '0.0.0.0').strip()

    def __str__(self):
        return f"{self.host}:{self.port}"

    def __repr__(self):
        return f"{type(self).__name__}(host={self.host}, ip={self.ip}, port={self.port})"

    @property
    def ip(self):
        if self._ip is None:
            self._ip = socket.gethostbyname(self.host)
        return self._ip

    def equivalent_to(self, other):
        return self.ip == other.ip and self.port == other.port

    @classmethod
    def parse(cls, address: str):
        host, port = address.split(":")
        return cls(host, int(port))

    @classmethod
    def local_port_on_any_interface(cls, port: int):
        return cls("0.0.0.0", port)

    @classmethod
    def localhost(cls, port: int):
        return cls("localhost", port)

    @classmethod
    def any_local_port(cls):
        return cls("", 0)

    def as_tuple(self):
        return self.ip, self.port


class Session(Protocol):

    @property
    def local_address(self) -> Address:
        ...

    @property
    def remote_address(self) -> Address:
        ...

    def send(self, payload: bytes | str):
        ...

    def receive(self, decode=True):
        ...

    def close(self):
        ...

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


class Server(Protocol):
    def __init__(self, port: int):
        ...

    def listen(self) -> Session:
        ...

    def receive(self, decode=True) -> tuple[str | bytes | None, Address | None]:
        ...

    def send(self, address: Address, payload: bytes | str):
        ...

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    def close(self):
        ...


class Client(Session):
    def __init__(self, remote_address: Address):
        ...
