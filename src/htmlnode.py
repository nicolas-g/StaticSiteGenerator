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
        # print(
        #     f"tag -> {self.tag} value -> {self.value} children -> {self.children}  props -> {self.props}"
        # )
        # print(
        #     f"href -> {self.props['href']} target-> {self.props['target']}"
        # )
        return f"href={self.props['href']} target={self.props['target']}"

    def __repr__(self):
        return f"self"
