from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "link.com"
    IMAGE = "imagine"


class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            (self.text == other.text)
            and (self.text_type == other.text_type)
            and (self.url == other.url)
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    if text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text)
    elif text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text)
    elif text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text)
    elif text_type == TextType.CODE:
        return LeafNode(tag="code", value=text)
    elif text_type == TextType.LINK:
        return LeafNode(tag="a", value=text, props={"href": url})
    elif text_type == TextType.IMAGE:
        return LeafNode(tag="img", value=text, props={"src": url, "alt": text})

    raise Exception(f"{text_node} is not type TextType")
