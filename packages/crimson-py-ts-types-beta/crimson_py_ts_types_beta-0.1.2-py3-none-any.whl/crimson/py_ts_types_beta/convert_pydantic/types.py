from typing import TypedDict, Any, Literal, Dict


class StringDict(TypedDict):
    """
    Stringified `pydantic.fields.FieldInfo`
    """

    annotation: str | None
    default: Any
    description: str | None
    required: Literal["True", "False"]


class StringFields(Dict[str, StringDict]):
    """
    key: name of the field
    value: `StringDict` of the field
    """
