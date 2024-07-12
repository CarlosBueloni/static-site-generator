import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
            
    
    def test_value_none(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_no_tag(self):
        node = LeafNode(value="this is raw text")
        self.assertEqual(node.to_html(), "this is raw text")
    
    
