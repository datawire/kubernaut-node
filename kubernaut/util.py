from typing import TypeVar

T = TypeVar('T')


def require(value: T, msg="Value cannot be None") -> T:
    if value is None:
        raise ValueError(msg)
    else:
        return value


def require_not_empty(value: T, msg="Value cannot be empty") -> T:
    if len(value) == 0:
        raise ValueError(msg)
    else:
        return value
