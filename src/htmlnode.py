from typing import List, Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[dict] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child class should overwrite this method")

    def props_to_html(self):
        html_props = []
        for key, value in self.props.items():
            # important to leave a leading space
            html_props.append(f' {key}="{value}"')
        return "".join(html_props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: Optional[dict] = None,
    ):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return self.value

        html_props = self.props_to_html() if self.props else ""
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: List[HTMLNode],
        props: Optional[dict] = None,
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")

        if not self.children:
            raise ValueError(
                "All parent nodes must have children, else they are children"
            )

        html_props = self.props_to_html() if self.props else ""
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{html_props}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
