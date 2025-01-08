import unittest

from textnode import TextNode, TextType
from constants import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_to_html_not_impl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_props_to_html(self):
        node = TextNode("This is a text node", "hello")
        self.assertEqual(node.text_type, TextType.DEFAULT.value)

if __name__ == "__main__":
    unittest.main()
