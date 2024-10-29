from typing import List
from textwrap import dedent


def convert_py_to_ts_comment_lines(
    comment: str, splitter: str = "\\n", dedented: bool = False
) -> List[str]:
    if dedented:
        comment = dedent(comment)

    start_buffer = "/**"
    end_buffer = " */"
    buffer = " * "

    split = comment.split(splitter)

    if len(split) > 1:
        split = split[1:-1]

    lines = []

    for line in split:
        lines.append(buffer + line)

    return [start_buffer] + lines + [end_buffer]
