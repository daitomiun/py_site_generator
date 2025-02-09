from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType

A_TAG="a"
A_VALUE="hello from boot.dev!"
A_CHILDREN=[]
A_PROPS={
    "href": "https://www.google.com", 
    "target": "_blank",
}
A_WITH_TAG_PROPS_HTML = """<a href="https://www.google.com" target="_blank">hello from boot.dev!</a>"""
A_VALUE_HTML = A_VALUE
A_WITHOUT_PROPS_HTML = """<a>hello from boot.dev!</a>"""

EXPECTED_PROPS = ' href="https://www.google.com" target="_blank"' 
EXPECTED_NONE_PROPS = ""
EXPECTED_VALUE = A_VALUE

EXPECTED_TEXT_NODE = TextNode(A_VALUE, TextType.DEFAULT)
EXPECTED_HTML_NODE = HTMLNode(tag=A_TAG, value=EXPECTED_TEXT_NODE.text, props=A_PROPS)


SIMPLE_PARENT_NODE=ParentNode( "p", [ LeafNode("b", "Hello") ])
SIMPLE_PARENT_NODE_RESULT="<p><b>Hello</b></p>"

SIMPLE_PARENT_NODE_WITH_PROPS=ParentNode( "div", [LeafNode("p", "text")], {"class": "container", "id": "main"})
SIMPLE_PARENT_NODE_WITH_PROPS_RESULT='<div class="container" id="main"><p>text</p></div>'
PARENT_NODE=ParentNode("div", [ LeafNode("span", "hello"), ParentNode("p", [ LeafNode("b", "world") ]) ])
PARENT_NODE_RESULT="<div><span>hello</span><p><b>world</b></p></div>"

COMPLEX_PARENT_NODE=ParentNode("div", [ LeafNode("h1", "Title"), ParentNode("section", [ LeafNode("p", "First paragraph"), ParentNode("div", [ LeafNode("span", "Nested span"), LeafNode("b", "Bold text"), LeafNode(None, "Normal text") ]), LeafNode("i", "Italic text") ]), LeafNode(None, "Footer text") ])
COMPLEX_PARENT_NODE_RESULT="<div><h1>Title</h1><section><p>First paragraph</p><div><span>Nested span</span><b>Bold text</b>Normal text</div><i>Italic text</i></section>Footer text</div>"

INVALID_NODE_EMPTY_TAG=ParentNode("", [LeafNode("b", "test")])
INVALID_NODE_NONE_TAG=ParentNode(None, [LeafNode("b", "test")])

INVALID_NODE_EMPTY_CHILDREN=ParentNode("div", [])
INVALID_NODE_NONE_CHILDREN=ParentNode("div", None)
INVALID_NODE_NO_LIST_CHILDREN=ParentNode("div", "not a list")
INVALID_NODE_NOT_A_HTML_NODE=ParentNode("div", [ "Just a string", LeafNode("p", "Valid node"), 42,  {"key": "value"} ])

