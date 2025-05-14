import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a test", [], {
                        "href": "https://www.google.com"})
        # node2 = HTMLNode("This is a text node", TextType.BOLD)
        # self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
