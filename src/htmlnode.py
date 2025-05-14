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
            print("props is none")
            return ""
        return_string = []
        for key, value in self.props.items():
            return_string.append(f'{key}="{value}"')
        return f" ".join(return_string)

    def __repr__(self):
        return f"{self}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        if self.tag == "a":
            return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        if self.tag == "img":
            print("Image detected!!")
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
