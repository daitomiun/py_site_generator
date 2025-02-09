from leafnode import LeafNode
from parentnode import ParentNode
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def main():
    # 1st check
    node = ParentNode( "div", [LeafNode("p", "text")], {"class": "container", "id": "main"})
    print(f"RESULT: {node.to_html()}")
    print("---------------------------------")
    text_node = TextNode("hello", TextType.BOLD)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("hello", TextType.ITALIC)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("hello", TextType.TEXT)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("print(hello)", TextType.CODE)
    print(repr(text_node_to_html_node(text_node)))
    text_node = TextNode("hello", TextType.LINK, "https://www.boot.dev")
    print("---------------------------------")
    print(repr(text_node_to_html_node(text_node)))
    text_node = TextNode("hello", TextType.IMAGE, "https://www.example.com/image.png")
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
main()
