import ast
from pydantic import BaseModel
from typing import Dict, Type, Optional
import inspect
from crimson.ast_dev_tool import collect_nodes


class AnnAssignStr(BaseModel):
    target: str
    annotation: Optional[str] = None
    value: Optional[str] = None


def get_ann_assign(ann_assign_node: ast.AnnAssign) -> AnnAssignStr:
    targets = ["target", "annotation", "value"]
    data = {}

    for target in targets:
        if hasattr(ann_assign_node, target):
            value = getattr(ann_assign_node, target)
            if isinstance(value, ast.AST):
                data[target] = ast.unparse(value)
    return AnnAssignStr(**data)


def get_original_annotations(class_node: ast.ClassDef) -> Dict[str, AnnAssignStr]:
    output = {}

    for node in class_node.body:
        if isinstance(node, ast.AnnAssign):
            model = get_ann_assign(node)
            output[model.target] = model
    return output


def recover_original_annotation(
    string_fields: Dict[str, Dict[str, str]],
    original_annotation: Dict[str, AnnAssignStr],
):
    for key, value in string_fields.items():
        value["annotation"] = original_annotation[key].annotation


def recover_original_annotations(
    model_obj: Type[BaseModel], string_fields: Dict[str, Dict[str, str]]
):
    model_code = inspect.getsource(model_obj)
    class_node = collect_nodes(model_code, ast.ClassDef)[0]
    original_annotations = get_original_annotations(class_node)
    recover_original_annotation(string_fields, original_annotations)
