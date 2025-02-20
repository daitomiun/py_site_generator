import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if len(delimiter) == 0 or delimiter == "":
        raise ValueError(f"Invalid empty delimeter")

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            break
        pos = 0
        while pos < len(node.text):
            start = node.text.find(delimiter, pos)
            if start == -1:
                new_nodes.append(TextNode(text=node.text[pos:], text_type=TextType.TEXT))
                break
            new_nodes.append(TextNode(text=node.text[pos:start], text_type=TextType.TEXT))

            end = node.text.find(delimiter, start + len(delimiter))
            if end == -1:
                raise ValueError("Unclosed delimiter")

            new_nodes.append(TextNode(text=node.text[start + len(delimiter):end], text_type=text_type))
            pos = end + len(delimiter)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 

def split_nodes_image(old_nodes):
    return get_split_nodes(
        old_nodes,
        TextType.IMAGE,
        extract_markdown_images,
        "![", "]", "(", ")"
    )
def split_nodes_link(old_nodes):
    return get_split_nodes(
        old_nodes,
        TextType.LINK,
        extract_markdown_links,
        "[", "]", "(", ")"
    )

def get_split_nodes(old_nodes, text_type, extract, left_delimiter, right_delimiter, url_left, url_right):
    """Split text nodes based on markdown patterns for links or images.
    
    Args:
        old_nodes (list): List of TextNode objects to process
        text_type (TextType): Type of node to create (LINK or IMAGE)
        extract (function): Function to extract markdown content (links or images)
        left_delimiter (str): Opening delimiter (e.g. "[" or "![")
        right_delimiter (str): Closing delimiter for alt text ("]")
        url_left (str): Opening delimiter for URL ("(")
        url_right (str): Closing delimiter for URL (")")
    
    Returns:
        list: New list of TextNode objects with markdown content split into separate nodes
    
    Example:
        >>> nodes = [TextNode("Hello [world](url)", TextType.TEXT)]
        >>> get_split_nodes(nodes, TextType.LINK, extract_markdown_links, "[", "]", "(", ")")
        [TextNode("Hello ", TextType.TEXT), TextNode("world", TextType.LINK, "url")]
    """
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        while current_text != "":
            links = extract(current_text) # <-- method for the extraction type
            if len(links) == 0:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
                break

            alt, url = links[0]
            sections = current_text.split(f"{left_delimiter}{alt}{right_delimiter}{url_left}{url}{url_right}", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, text_type, url))
            current_text = sections[1]

    return new_nodes

