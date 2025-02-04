from htmlnode import HTMLNode
from textnode import TextNode, TextType


A_TAG="a"
A_VALUE="hello from boot.dev!"
A_CHILDREN=[]
A_PROPS={
    "href": "https://www.google.com", 
    "target": "_blank",
}
A_WITH_TAG_PROPS_HTML = """<a href="https://www.google.com" target="_blank" >hello from boot.dev!</a>"""
A_VALUE_HTML = A_VALUE
A_WITHOUT_PROPS_HTML = """<a >hello from boot.dev!</a>"""

EXPECTED_PROPS = """href="https://www.google.com" target="_blank" """
EXPECTED_NONE_PROPS = ""
EXPECTED_VALUE = A_VALUE

EXPECTED_TEXT_NODE = TextNode(A_VALUE, TextType.DEFAULT)
EXPECTED_HTML_NODE = HTMLNode(tag=A_TAG, value=EXPECTED_TEXT_NODE.text, props=A_PROPS)

