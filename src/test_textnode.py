import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node3)
        node4 = TextNode("This is a different text node", TextType.LINK, "http://test.com")
        node5 = TextNode("This is a different text node", TextType.LINK, "http://test.com")
        self.assertEqual(node4, node5)


if __name__ == "__main__":
    unittest.main()
