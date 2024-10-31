import os
from typing import Callable, TypeVar, cast, overload

from hayai.loader import Loader


T = TypeVar("T", bound=Callable)


@overload
def hayai(func: T) -> T: ...


@overload
def hayai(
    *,
    workers: int = 2 * os.cpu_count() or 8,
    queue_size: int = 2 * os.cpu_count() or 8,
) -> Callable[[T], T]: ...


def hayai(
    func: T | None = None,
    *,
    workers: int = 2 * os.cpu_count() or 8,
    queue_size: int = 2 * os.cpu_count() or 8,
) -> T | Callable[[T], T]:
    def decorator(func: T) -> T:
        loader = Loader(func, workers=workers, queue_size=queue_size)
        return cast(T, loader)

    if func is None:
        return decorator
    return decorator(func)
