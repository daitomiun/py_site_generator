from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
    tag, props, value = get_tag_props_from_node(text_node)
    if tag is None and props is None:
        return LeafNode(value=text_node.text)
    return LeafNode(tag=tag, value=value, props=props)

def get_tag_props_from_node(node):
    match(node.text_type):
        case TextType.BOLD:
            return "b", None, node.text
        case TextType.TEXT:
            return None, None, node.text
        case TextType.ITALIC:
            return "i", None, node.text
        case TextType.CODE:
            return "code", None, node.text
        case TextType.LINK:
            return "a", {"href": node.url}, node.text
        case TextType.IMAGE:
            return "img", {"src": node.url, "alt": node.text }, ""
        case _:
            raise ValueError("ERR: Not valid Text Type")

