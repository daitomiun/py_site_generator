from constants import A_PROPS, A_TAG, A_VALUE
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def main():
    textNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    print(repr(textNode))

    test_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    html_node = HTMLNode(props=test_props)
    props = html_node.props_to_html()
    print(props)

    html_leaf_node = LeafNode(tag=A_TAG, value=A_VALUE, props=A_PROPS)
    print(html_leaf_node.to_html())

main()
