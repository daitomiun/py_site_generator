import unittest

from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextTo_HTMLNode(unittest.TestCase):
    def test_valid_bold_type(self):
        text_node = TextNode("hello", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        
        self.assertEqual(html_node.tag, "b")
        self.assertIsNone(html_node.props)
        self.assertEqual(html_node.value, "hello")

    def test_valid_link_type(self):
        text_node = TextNode("hello", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_valid_img_type(self):
        text_node = TextNode("hello", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "hello" })

    def test_valid_text_type(self):
        text_node = TextNode("hello", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "hello")
        self.assertIsNone(html_node.props)

    def test_invalid_type(self):
        with self.assertRaisesRegex(ValueError,"ERR: text_type in the text node needs to be of TextType"):
            TextNode("hello", "INVALID_BOLD")

if __name__ == "__main__":
    unittest.main()
