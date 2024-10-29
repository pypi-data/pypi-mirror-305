import types
from typing import *

__all__ = ["makefunc"]


def makefunc(cls: type) -> types.FunctionType:
    obj = cls()

    def ans(*args: Any, **kwargs: Any):
        return obj(*args, **kwargs)

    ans.__module__ = cls.__module__
    ans.__name__ = cls.__name__
    ans.__qualname__ = cls.__qualname__
    ans.__doc__ = obj.__call__.__doc__
    ans.__annotations__ = obj.__call__.__annotations__
    ans.__wrapped__ = obj.__call__
    return ans
