import unittest

from leafnode import LeafNode
from constants import *

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_node_no_props(self):
        html_leaf_node = LeafNode(tag=A_TAG, value=A_VALUE)
        self.assertEqual(html_leaf_node.to_html(), A_WITHOUT_PROPS_HTML)

    def test_leaf_node_to_html_with_tag_props(self):
        html_leaf_node = LeafNode(tag=A_TAG, value=A_VALUE, props=A_PROPS)
        self.assertEqual(html_leaf_node.to_html(), A_WITH_TAG_PROPS_HTML)

    def test_leaf_node_to_html_without_tag(self):
        html_leaf_node = LeafNode(value=A_VALUE, props=A_PROPS)
        self.assertEqual(html_leaf_node.to_html(), A_VALUE_HTML)


    def test_leaf_node_to_html_none_values(self):
        html_leaf_node = LeafNode()
        self.assertEqual(html_leaf_node.props_to_html(), EXPECTED_NONE_PROPS)

if __name__ == "__main__":
    unittest.main()
