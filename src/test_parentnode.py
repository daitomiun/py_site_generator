import unittest
from constants import *

class TestParentNode(unittest.TestCase):
    def test_parent_node_simple_node(self):
        html_parent_node = SIMPLE_PARENT_NODE
        self.assertEqual(html_parent_node.to_html(), SIMPLE_PARENT_NODE_RESULT)

    def test_parent_node_simple_node_with_props(self):
        html_parent_node = SIMPLE_PARENT_NODE_WITH_PROPS
        self.assertEqual(html_parent_node.to_html(), SIMPLE_PARENT_NODE_WITH_PROPS_RESULT)

    def test_parent_node(self):
        html_parent_node = PARENT_NODE
        self.assertEqual(html_parent_node.to_html(), PARENT_NODE_RESULT)

    def test_parent_node_complex_node(self):
        html_parent_node = COMPLEX_PARENT_NODE
        self.assertEqual(html_parent_node.to_html(), COMPLEX_PARENT_NODE_RESULT)


    def test_invalid_parent_node_emtpy_tag(self):
        html_parent_node = INVALID_NODE_EMPTY_TAG
        with self.assertRaisesRegex(ValueError, "ERR: The parent Node needs a tag value"):
            html_parent_node.to_html()

    def test_invalid_parent_node_none_tag(self):
        html_parent_node = INVALID_NODE_NONE_TAG
        with self.assertRaisesRegex(ValueError, "ERR: The parent Node needs a tag value"):
            html_parent_node.to_html()

    def test_invalid_parent_node_empty_children(self):
        html_parent_node = INVALID_NODE_EMPTY_CHILDREN
        with self.assertRaisesRegex(ValueError, "ERR: The parent Node needs a valid children value"):
            html_parent_node.to_html()

    def test_invalid_parent_node_none_children(self):
        html_parent_node = INVALID_NODE_NONE_CHILDREN
        with self.assertRaisesRegex(ValueError, "ERR: The parent Node needs a valid children value"):
            html_parent_node.to_html()

    def test_invalid_parent_node_no_list_children(self):
        html_parent_node = INVALID_NODE_NO_LIST_CHILDREN
        with self.assertRaisesRegex(ValueError, "ERR: The parent Node needs a valid children value"):
            html_parent_node.to_html()

    def test_invalid_parent_node_not_a_HTML_NODE(self):
        html_parent_node = INVALID_NODE_NOT_A_HTML_NODE
        with self.assertRaisesRegex(ValueError, "ERR: All children must be HTMLNode objects"):
            html_parent_node.to_html()
if __name__ == "__main__":
    unittest.main()
