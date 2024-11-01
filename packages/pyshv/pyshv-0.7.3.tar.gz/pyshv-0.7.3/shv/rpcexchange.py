"""RPC Exchange usage and implementation utility."""

from __future__ import annotations

from .simplebase import SimpleBase


class RpcExchange:
    """RPC Exchange connection over :class:`SimpleBase`."""

    def __init__(
        self,
        client: SimpleBase,
        path: str,
        token: str,
    ) -> None:
        self.client: SimpleBase = client
        """The client used to access the RPC file."""
        self._path = f"{path}/{token}"
        self._wbuf: bytearray = bytearray()
        self._rbuf: bytearray = bytearray()

    async def read(self, n: int = -1) -> bytes:
        """Read bytes from the exchange stream.

        This also sends any bytes that were previously written.
        """
        return b""

    # TODO readline, readexactly, and readuntil

    def write(self, data: bytes) -> None:
        """Write bytes to the exchange stream."""

    async def drain(self) -> None:
        """Drain all written bytes to the exchange stream.

        RPC Exchange is designed to do read and write with a single operation
        where reading is required to be performed before write is allowed. This
        means that this function must buffer read data. In most cases it is
        better to use :meth:`read` directly instead of this one.
        """

    async def close(self) -> None:
        """Close the exchange stream."""
