from pydantic import BaseModel
from typing import _TypedDictMeta


def is_basemodel(obj: object) -> bool:
    candidates = [BaseModel]
    for candidate in candidates:
        if any([base is candidate for base in obj.__bases__]):
            return True
    return False


def is_typeddict(obj: object) -> bool:
    return type(obj) is _TypedDictMeta
