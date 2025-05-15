class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Child classes will override this method to render themselves as HTML
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or not self.props:
            return ""
        return_string = []
        for key, value in self.props.items():
            return_string.append(f'{key}="{value}"')
        joined_attributes = " ".join(return_string)
        return f" {joined_attributes}"

    def __repr__(self):
        return f"{self}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires a tag")
        if not self.children:
            raise ValueError("ParentNode requires children")

        opening_tag_html = f"<{self.tag}{self.props_to_html()}>"
        children_html_content = ""
        for child_node in self.children:
            children_html_content += child_node.to_html()

        closing_tag_html = f"</{self.tag}>"  #
        return f"{opening_tag_html}{children_html_content}{closing_tag_html}"
        # return f"{self(self.tag, self.value, self.props)}"
