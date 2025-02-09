import unittest

from htmlnode import HTMLNode
from constants import *
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    
    def test_props_eq(self):
        html_node = HTMLNode(props=A_PROPS)
        self.assertEqual(html_node.props_to_html(), EXPECTED_PROPS)

    def test_html_node_values(self):
        text_node = TextNode(A_VALUE, TextType.LINK)
        html_node = HTMLNode(tag=A_TAG, value=text_node.text, props=A_PROPS)

        result_html_node = repr(html_node)
        self.assertEqual(result_html_node, repr(EXPECTED_HTML_NODE))

    def test_none_props_to_html(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), EXPECTED_NONE_PROPS)

if __name__ == "__main__":
    unittest.main()
