from collections import defaultdict

from inkwell.api.page import PageFragment
from inkwell.components.document import (
    DocumentPageBlocks,
    PageBlocks,
    PageImage,
)


def split_layout_blocks(page_images: list[PageImage]) -> DocumentPageBlocks:
    document_page_blocks = []
    for page_image in page_images:
        page_image_blocks = PageBlocks(
            page_image=page_image.page_image,
            figure_blocks=[],
            table_blocks=[],
            text_blocks=[],
            page_number=page_image.page_number,
        )

        for block in page_image.page_layout.get_blocks():
            if block.type == "Figure":
                page_image_blocks.figure_blocks.append(block)
            elif block.type == "Table":
                page_image_blocks.table_blocks.append(block)
            else:
                page_image_blocks.text_blocks.append(block)

        document_page_blocks.append(page_image_blocks)

    return DocumentPageBlocks(page_blocks=document_page_blocks)


def combine_fragments(
    document_figure_fragments: list[PageFragment],
    document_table_fragments: list[PageFragment],
    document_text_fragments: list[PageFragment],
) -> dict[int, list[PageFragment]]:

    pages_map = defaultdict(list)
    for figure_fragment in document_figure_fragments:
        pages_map[figure_fragment.page_number].append(figure_fragment)
    for table_fragment in document_table_fragments:
        pages_map[table_fragment.page_number].append(table_fragment)
    for text_fragment in document_text_fragments:
        pages_map[text_fragment.page_number].append(text_fragment)

    return pages_map


def convert_table_dict_to_markdown(table_dict: dict) -> str:

    header_row = table_dict["header"]
    rows = table_dict["rows"]

    # Calculate maximum width for each column
    col_widths = []
    for idx, row in enumerate(header_row):
        column_values = [str(row)] + [str(row[idx]) for row in rows]
        col_widths.append(max(len(value) for value in column_values))

    result = "|"
    for header, width in zip(header_row, col_widths):
        result += f" {header:<{width}} |"
    result += "\n|"

    for width in col_widths:
        result += f" {'-' * width} |"
    result += "\n"

    for row in rows:
        result += "|"
        for item, width in zip(row, col_widths):
            result += f" {str(item):<{width}} |"
        result += "\n"

    return result
