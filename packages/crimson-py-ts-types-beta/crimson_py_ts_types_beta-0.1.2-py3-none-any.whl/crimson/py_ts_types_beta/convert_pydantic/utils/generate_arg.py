from crimson.py_ts_types_beta.convert_typing import convert_py_to_ts
from typing import List
from crimson.py_ts_types_beta.convert_pydantic.types import StringDict
from crimson.py_ts_types_beta.convert_pydantic.utils.comment import (
    convert_py_to_ts_comment_lines,
)


def generate_arg_description_lines(string_dict: StringDict) -> List[str] | None:
    if "description" not in string_dict.keys():
        return None

    description: str = string_dict["description"][1:-1]

    return convert_py_to_ts_comment_lines(description)


def generate_arg(name: str, string_dict: StringDict) -> str:
    template = f"{name}"
    if string_dict["required"] == "False":
        template = template + "?"
    return template


def generate_annotation(annotation: str) -> str:
    annotation = convert_py_to_ts(annotation)
    return f":{annotation}"


def generate_arg_line(name: str, string_dict: StringDict) -> str:

    return generate_arg(name, string_dict) + generate_annotation(
        string_dict["annotation"]
    )


def generate_arg_lines(name: str, string_dict: StringDict, indent=4) -> List[str]:

    arg_lines = [generate_arg_line(name, string_dict)]

    description_lines = generate_arg_description_lines(string_dict)
    if description_lines is not None:
        arg_lines = description_lines + arg_lines

    lines = indent_lines(arg_lines, indent)

    return lines


def generate_arg_final(name: str, string_dict: StringDict, indent=4) -> str:
    arg_lines = generate_arg_lines(name, string_dict, indent)
    return "\n".join(arg_lines)


def indent_lines(lines: List[str], indent=4) -> List[str]:
    indent = " " * indent
    lines = [indent + line for line in lines]
    return lines
