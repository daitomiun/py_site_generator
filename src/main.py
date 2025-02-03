from htmlnode import HTMLNode
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
    

main()
