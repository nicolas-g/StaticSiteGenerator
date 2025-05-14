from textnode import TextNode, TextType


def main():
    TNode = TextNode("This is some anchor text",
                     TextType.LINK, "https://www.boot.dev")
    print(TNode)


if __name__ == "__main__":
    main()
