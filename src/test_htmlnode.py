import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a test", [], {
                        "href": "https://www.google.com"})
        # node2 = HTMLNode("This is a text node", TextType.BOLD)
        # self.assertEqual(node, node2)
        #


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node2.to_html(), "<p>This is a paragraph of text.</p>")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node3.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")


if __name__ == "__main__":
    unittest.main()
