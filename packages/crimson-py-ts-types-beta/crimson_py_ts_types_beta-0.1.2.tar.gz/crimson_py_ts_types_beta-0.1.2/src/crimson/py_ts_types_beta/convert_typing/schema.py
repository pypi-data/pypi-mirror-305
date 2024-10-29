from pydantic import BaseModel
from typing import Dict, Union, Type, Tuple, Literal, List, Optional


class WithElts(BaseModel):
    name: str
    open: str = "<"
    close: str = ">"
    separator: Literal["|", ","] = ","


class WithSlice(BaseModel):
    name: str
    open: str = "<"
    close: str = ">"


with_elts_schemas: Dict[Type, Union[WithElts]] = {
    Union: WithElts(name="Union", separator="|"),
    Tuple: WithElts(name="Tuple", open="<[", close="]>"),
    Dict: WithElts(name="Dict"),
    Literal: WithElts(name="Literal", separator="|"),
}

with_slice_schemas: Dict[Type, Union[WithSlice]] = {
    List: WithSlice(name="List",),
    Optional: WithSlice(name=Optional.__name__)
}

schemas = with_elts_schemas.copy()
schemas.update(with_slice_schemas)


def convert_schemas_keys(
    schemas: Dict[Type, Union[WithElts, WithSlice]]
) -> Dict[str, Union[WithElts, WithSlice]]:
    return {key.__name__: value for key, value in schemas.items()}


class SchemaHolder:
    with_elts_schemas = with_elts_schemas
    with_slice_schemas = with_slice_schemas
    schemas: Dict[Type, Union[WithElts, WithSlice]] = schemas
    converted_schemas = convert_schemas_keys(schemas)
