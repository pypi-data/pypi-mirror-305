from typing import Dict
import ast
from crimson.py_ts_types_beta.convert_pydantic.types import StringFields
from crimson.ast_dev_tool import collect_nodes
from pydantic.fields import FieldInfo


def convert_fieldinfo_to_string_dict(field_info: FieldInfo) -> Dict[str, str]:
    code = repr(field_info)
    call_node = collect_nodes(code, ast.Call)[0]
    output = {}
    for keyword in call_node.keywords:
        output[keyword.arg] = ast.unparse(keyword.value)
    return output


def get_string_fields(model_fields: Dict[str, FieldInfo]) -> StringFields:
    string_fields = {}
    for arg, field_info in model_fields.items():
        string_fields[arg] = convert_fieldinfo_to_string_dict(field_info)

    return string_fields
