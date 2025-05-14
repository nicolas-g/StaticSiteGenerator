from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    TNode = TextNode("This is some anchor text",
                     TextType.LINK, "https://www.boot.dev")

    print(TNode)

    HNode = HTMLNode("p", "This is some anchor text", "none", {"href": "https://www.google.com","target": "_blank",})
    HNode.props_to_html()


if __name__ == "__main__":
    main()
