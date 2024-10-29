from pydantic import BaseModel
from typing import Type
from crimson.py_ts_types_beta.convert_pydantic.utils.recover_annotation import (
    recover_original_annotations,
)
from crimson.py_ts_types_beta.convert_pydantic.utils.generate_arg import (
    generate_arg_lines,
)
from crimson.py_ts_types_beta.convert_pydantic.types import StringDict
from crimson.py_ts_types_beta.convert_pydantic.utils.generate_string_field import (
    get_string_fields,
)
from crimson.py_ts_types_beta.convert_pydantic.utils.comment import (
    convert_py_to_ts_comment_lines,
)


def generate_interface(
    model_obj: Type[BaseModel], original_annotation: bool = True, indent: int = 4
) -> str:

    start = """interface {name}""".format(name=model_obj.__name__) + " {"

    if model_obj.__doc__ is not None:
        ts_description = convert_py_to_ts_comment_lines(
            model_obj.__doc__, splitter="\n", dedented=True
        )
        start = "\n".join(ts_description + [start])

    string_fields = get_string_fields(model_obj.model_fields)

    if original_annotation:
        recover_original_annotations(model_obj, string_fields)

    all_arg_lines = []

    for name, string_dict in string_fields.items():
        all_arg_lines = all_arg_lines + generate_arg_lines(name, string_dict, indent)

    end = "}"

    return "\n".join([start] + all_arg_lines + [end])


def generate_default_line(name: str, string_dict: StringDict) -> str | None:
    if "default" in string_dict.keys():
        return f"{name} = {string_dict['default']}"
    else:
        None


def generate_default(model_obj: Type[BaseModel], indent: int = 4) -> str:
    start = """const default{name}: {name}""".format(name=model_obj.__name__) + " {"
    string_fields = get_string_fields(model_obj.model_fields)
    arg_lines = [
        " " * indent + generate_default_line(name, string_dict)
        for name, string_dict in string_fields.items()
        if generate_default_line(name, string_dict) is not None
    ]
    end = "}"

    return "\n".join([start] + arg_lines + [end])
