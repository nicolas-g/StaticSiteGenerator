import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a test", [], {"href": "https://www.google.com"})
        # node2 = HTMLNode("This is a text node", TextType.BOLD)
        # self.assertEqual(node, node2)
        #


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node2.to_html(), "<p>This is a paragraph of text.</p>")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node3.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_assignment_example(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                # LeafNode with no tag renders raw text
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_html = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(node.to_html(), expected_html)

    # New test: ParentNode with properties
    def test_to_html_with_props(self):
        node = ParentNode(
            "div", [LeafNode("p", "Hello")], {"class": "container", "id": "main-div"}
        )
        # Remember props_to_html() adds a leading space if props exist,
        # and orders them based on dictionary iteration (which is insertion order for Python 3.7+)
        # For consistency, you might sort keys if order matters, but usually it doesn't for HTML attributes.
        # Let's assume current dict iteration order:
        expected_html = '<div class="container" id="main-div"><p>Hello</p></div>'
        # If your dict order was different, it might be '<div id="main-div" class="container">...
        # A more robust test for props might check for inclusion of each prop string
        # rather than exact string match if dict order is not guaranteed or relevant.
        # However, for this assignment, direct string comparison is likely fine.
        self.assertEqual(node.to_html(), expected_html)

    # New test: Deeper nesting with multiple children at different levels
    def test_to_html_deeper_nesting(self):
        node = ParentNode(
            "body",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("h1", "Title"),
                        ParentNode(
                            "p",
                            [
                                LeafNode(None, "Some text and a "),
                                LeafNode("a", "link", {"href": "#"}),
                            ],
                        ),
                    ],
                ),
                ParentNode("footer", [LeafNode(None, "Copyright")]),
            ],
        )
        expected_html = '<body><div><h1>Title</h1><p>Some text and a <a href="#">link</a></p></div><footer>Copyright</footer></body>'
        self.assertEqual(node.to_html(), expected_html)

    # New test: Error case - No tag
    def test_to_html_no_tag_raises_value_error(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaisesRegex(ValueError, "ParentNode requires a tag"):
            node.to_html()

    # New test: Error case - No children (empty list)
    def test_to_html_no_children_empty_list_raises_value_error(self):
        node = ParentNode("div", [])  # Empty list for children
        # Corrected message
        with self.assertRaisesRegex(ValueError, "ParentNode requires children"):
            node.to_html()

    # New test: Error case - No children (None)
    def test_to_html_no_children_none_raises_value_error(self):
        node = ParentNode("div", None)  # None for children
        # Corrected message
        with self.assertRaisesRegex(ValueError, "ParentNode requires children"):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
