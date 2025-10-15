from pathlib import Path
from posixpath import isfile

from markdown_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block.startswith("# "):
            return block[2:].strip()
    raise ValueError("No title found")


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)
    for content_path in dir_path_content.iterdir():
        complete_path = dest_dir_path / content_path.relative_to(dir_path_content)
        if content_path.is_file():
            generate_page(
                content_path, template_path, complete_path.with_suffix(".html")
            )
        else:
            generate_pages_recursive(content_path, template_path, complete_path)
