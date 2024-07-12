import  unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("a", "this is a link", props={"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "this is a link")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_repr(self):
        node = str(HTMLNode("a", "this is a link", props={"href": "https://www.google.com"}))
        self.assertEqual(node, "HTMLNode(a, this is a link, children: None, {'href': 'https://www.google.com'})")

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode("a", "this is a link", props={"href": "https://www.google.com"})
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("a", "this is a link", props={"href": "https://www.google.com",
                                                        "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_to_html(self):
        node = HTMLNode("a", "this is a link")
        self.assertEqual(node.props_to_html(), "")
