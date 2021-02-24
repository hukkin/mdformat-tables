from collections import OrderedDict
from typing import List, Optional, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdformat.renderer import MARKERS, MDRenderer


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    mdit.enable("table")


def _parse_cells(
    rows: List[List[List[Token]]], renderer: MDRenderer, options: dict, env: dict
) -> List[List[str]]:
    """Convert tokens in each cell to strings."""
    for i, row in enumerate(rows):
        for j, cell_tokens in enumerate(row):
            rows[i][j] = (
                renderer.render(
                    cell_tokens,
                    options,
                    env,
                    finalize=False,
                )
                .replace(MARKERS.BLOCK_SEPARATOR, "")
                .rstrip()
            )
    return rows


def _to_string(rows: List[List[str]], align: List[str], widths: dict) -> List[str]:
    lines = []
    lines.append(
        "| "
        + " | ".join(
            f"{{:{al or '<'}{widths[i]}}}".format(text)
            for i, (text, al) in enumerate(zip(rows[0], align[0]))
        )
        + " |"
    )
    lines.append(
        "| "
        + " | ".join(
            (":" if al in ("<", "^") else "-")
            + "-" * (widths[i] - 2)
            + (":" if al in (">", "^") else "-")
            for i, al in enumerate(align[0])
        )
        + " |"
    )
    for row, als in zip(rows[1:], align[1:]):
        lines.append(
            "| "
            + " | ".join(
                f"{{:{al or '<'}{widths[i]}}}".format(text)
                for i, (text, al) in enumerate(zip(row, als))
            )
            + " |"
        )
    return lines


def render_token(  # noqa: C901
    renderer: MDRenderer,
    tokens: List[Token],
    index: int,
    options: dict,
    env: dict,
) -> Optional[Tuple[str, int]]:
    """Convert token(s) to a string, or return None if no render method available.

    :returns: (text, index) where index is of the final "consumed" token
    """
    if tokens[index].type != "table_open":
        return None

    # gather all cell tokens into row * column array
    rows = []
    align = []
    while True:
        index += 1
        if index >= len(tokens) or tokens[index].type == "table_close":
            break
        if tokens[index].type == "tr_open":
            rows.append([])
            align.append([])
            continue
        for tag in ["th", "td"]:
            if tokens[index].type != f"{tag}_open":
                continue
            rows[-1].append([])
            style = tokens[index].attrGet("style") or ""
            if "text-align:right" in style:
                align[-1].append(">")
            elif "text-align:left" in style:
                align[-1].append("<")
            elif "text-align:center" in style:
                align[-1].append("^")
            else:
                align[-1].append("")
            inline_token = tokens[index + 1]
            rows[-1][-1].append(inline_token)
            while True:
                index += 1
                if index >= len(tokens) or tokens[index].type == f"{tag}_close":
                    break

    # parse all cells
    rows = _parse_cells(rows, renderer, options, env)

    # work out the widths for each column
    widths = OrderedDict()
    for row in rows:
        for j, cell_text in enumerate(row):
            widths[j] = max(widths.get(j, 3), len(cell_text))

    # write content
    # note: assuming always one header row
    lines = _to_string(rows, align, widths)

    return "\n".join(lines) + MARKERS.BLOCK_SEPARATOR, index
