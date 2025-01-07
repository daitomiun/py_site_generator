import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_diff_text_type(self):
        node = TextNode("This is a text node", "hello")
        self.assertEqual(node.text_type, TextType.DEFAULT.value)

if __name__ == "__main__":
    unittest.main()
