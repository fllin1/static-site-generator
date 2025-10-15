import re
from typing import List

from textnode import TextNode, TextType


def extract_markdown_images(text: str):
    images = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    for match in matches:
        alt = match[0][:]
        url = match[1][:]
        images.append((alt, url))
    return images


def extract_markdown_links(text: str):
    links = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    for match in matches:
        alt = match[0][:]
        url = match[1][:]
        links.append((alt, url))
    return links


def split_nodes_delimiter(
    old_nodes: List[TextNode],
    delimiter: str,
    text_type: TextType,
):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        buffer = old_node.text.split(delimiter)
        if len(buffer) % 2 != 1:
            raise Exception(f"{old_node.text} is an invalid Markdown")
        for i in range(len(buffer)):
            if not buffer[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(buffer[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(buffer[i], text_type))
    return new_nodes


def split_nodes_image(old_nodes: List[TextNode]):
    new_nodes = []
    buffer = [None]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        temp_text = old_node.text
        for image in images:
            alt, url = image
            buffer = temp_text.split(f"![{alt}]({url})")
            if len(buffer) != 2:
                raise ValueError("fix your split nodes image")
            if buffer[0]:
                new_nodes.append(TextNode(buffer[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            temp_text = buffer[1]
        if buffer[1]:
            new_nodes.append(TextNode(buffer[1], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: List[TextNode]):
    new_nodes = []
    buffer = [None]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        temp_text = old_node.text
        for link in links:
            alt, url = link
            buffer = temp_text.split(f"[{alt}]({url})")
            if len(buffer) != 2:
                raise ValueError("fix your split nodes links")
            if buffer[0]:
                new_nodes.append(TextNode(buffer[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            temp_text = buffer[1]
        if buffer[1]:
            new_nodes.append(TextNode(buffer[1], TextType.TEXT))
    return new_nodes


def text_to_textnodes(text: str):
    node = TextNode(text, TextType.TEXT)
    get_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    get_italian = split_nodes_delimiter(get_bold, "_", TextType.ITALIC)
    get_code = split_nodes_delimiter(get_italian, "`", TextType.CODE)
    get_imagine = split_nodes_image(get_code)
    get_linked = split_nodes_link(get_imagine)
    return get_linked
