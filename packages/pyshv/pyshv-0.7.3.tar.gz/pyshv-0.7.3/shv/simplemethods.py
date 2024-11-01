"""Class that provides an easier way to define regular methods and signals."""

from __future__ import annotations

import asyncio
import collections
import collections.abc
import dataclasses

from .rpcmethod import RpcMethodAccess, RpcMethodDesc
from .rpctransport import RpcClient
from .simplebase import SimpleBase
from .value import SHVType

RpcMethodFunc = collections.abc.Callable[
    [str, str, SHVType, RpcMethodAccess, str | None],
    SHVType | asyncio.Future[SHVType],
]


class SimpleMethods(SimpleBase):
    """SHV RPC methods and signals implementation helper.

    The regular way to implement methods in :class:`SimpleBase` is by defining
    `_ls`, `_dir`, and `_method_call` methods. That provides ability to
    implement discoverability as well as method implementation in various
    dynamic ways. But in real world applications it is common that we just want
    to define custom methods and having to implement these methods can be error
    prune and unnecessary complex. This class instead provides a way to define
    methods that are discovered and their integration is handled automatically.
    """

    def __init__(
        self,
        client: RpcClient,
        *args: typing.Any,  # noqa ANN401
        **kwargs: typing.Any,  # noqa ANN401
    ) -> None:
        super().__init__(client, *args, **kwargs)
        self.methods: dict[str, dict[str, SimpleMethods.Method]] = (
            collections.defaultdict(dict)
        )
        for attr in self.__dict__.values():
            match attr:
                case self.Method():
                    # TODO check if method doesn't already exist
                    self.methods[attr.path][attr.desc.name] = attr
                case self.Property():
                    self.methods[attr.path].update(attr.methods())

    async def _method_call(
        self,
        path: str,
        method: str,
        param: SHVType,
        access: RpcMethodAccess,
        user_id: str | None,
    ) -> SHVType:
        if path in self.methods:
            if method in self.methods[path]:
                res = self.methods[path][method].func(
                    path, method, param, access, user_id
                )
                if isinstance(res, asyncio.Future):
                    res = await res
                return res
        return await super()._method_call(path, method, param, access, user_id)

    def _ls(self, path: str) -> collections.abc.Iterator[str]:
        yield from super()._ls(path)
        for pth in self.methods:
            if not path or pth.startswith(path + "/"):
                yield pth[len(path) :].partition("/")[0]

    def _dir(self, path: str) -> collections.abc.Iterator[RpcMethodDesc]:
        yield from super()._dir(path)
        if path in self.methods:
            for method in self.methods[path].values():
                yield method.desc

    @dataclasses.dataclass
    class Method:
        """The definition of the RPC Method.

        This allows you to define methods as attributes of the object and such
        methods are automatically discovered and used.
        """

        path: str
        """
        """
        desc: RpcMethodDesc
        """
        """
        func: RpcMethodFunc
        """
        """

        def __get__(
            self, instance: SimpleMethods, owner: object
        ) -> collections.abc.Callable:
            return lambda *args, **kwargs: self(instance, *args, **kwargs)

        async def __call__(
            self,
            simple_methods: SimpleMethods,
            signal: str | None = None,
            value: SHVType = None,
            access: RpcMethodAccess = RpcMethodAccess.READ,
        ) -> None:
            """External call is used to send signals."""
            if signal is None:
                if not self.desc.signals:
                    raise NotImplementedError("Method doesn't have any signals")
                signal = next(iter(self.desc.signals.keys()))
            elif signal not in self.desc.signals:
                raise ValueError(f"Invalid signal name: {signal}")
            await simple_methods._signal(
                self.path, signal, self.desc.name, value, access
            )

    @classmethod
    def rpcmethod(
        cls, path: str, desc: RpcMethodDesc
    ) -> collections.abc.Callable[[RpcMethodFunc], SimpleBase.Method]:
        """Decorate method to turn it to :class:`SimpleMethods.Method`."""

        def decorator(func: RpcMethodFunc) -> SimpleBase.Method:
            return cls.Method(path, desc, func)

        return decorator

    @dataclasses.dataclass
    class Property:
        """The definition of the RPC Property node.

        This allows you to define methods as attributes of the object and such
        methods are automatically discovered and used.
        """

        path: str
        """
        """
        tp: str = "Any"
        """
        """
        access: RpcMethodAccess = RpcMethodAccess.READ
        """
        """
        signal: bool | str = False

        def setter(self) -> SimpleMethods.Property:
            # TODO decorate set method
            return self

        def __get__(
            self, instance: SimpleMethods, owner: object
        ) -> collections.abc.Callable:
            return lambda *args, **kwargs: self(instance, *args, **kwargs)

        async def __call__(
            self,
            simple_methods: SimpleMethods,
            value: SHVType = None,
        ) -> None:
            """External call is used to send signal."""
            if not self.signal:
                raise NotImplementedError("Method doesn't have any signals")
            await simple_methods._signal(
                self.path,
                "get",
                "chng" if isinstance(self.signal, bool) else self.signal,
                value,
                self.access,
            )

        def methods(self) -> dict[str, SimpleMethods.Method]:
            """Get methods for property implementation."""
            return {
                "get": SimpleMethods.Method(
                    self.path, RpcMethodDesc.getter(), self._get
                ),
                "set": SimpleMethods.Method(
                    self.path, RpcMethodDesc.setter(), self._set
                ),
            }

        def _get(
            self,
            path: str,
            method: str,
            param: SHVType,
            access: RpcMethodAccess,
            user_id: str | None,
        ) -> SHVType:
            return None

        def _set(
            self,
            path: str,
            method: str,
            param: SHVType,
            access: RpcMethodAccess,
            user_id: str | None,
        ) -> SHVType:
            return None
