import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    new_nodes = []
    delimiters = {
        "**": TextType.BOLD,
        "*": TextType.ITALIC, 
        "`": TextType.CODE
    }

    new_nodes = [TextNode(text, TextType.TEXT)]
    
    for delimiter in delimiters:
        new_nodes = split_nodes_delimiter(
            old_nodes=new_nodes,
            delimiter=delimiter,
            text_type=delimiters[delimiter]
        )
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if len(delimiter) == 0 or delimiter == "":
        raise ValueError(f"Invalid empty delimeter")

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        pos = 0
        while pos < len(node.text):
            start = node.text.find(delimiter, pos)
            if start == -1:
                new_nodes.append(TextNode(text=node.text[pos:], text_type=TextType.TEXT, url=node.url))
                break
            new_nodes.append(TextNode(text=node.text[pos:start], text_type=TextType.TEXT, url=node.url))

            end = node.text.find(delimiter, start + len(delimiter))
            if end == -1:
                raise ValueError("Unclosed delimiter")

            new_nodes.append(TextNode(text=node.text[start + len(delimiter):end], text_type=text_type, url=node.url))
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
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        if current_text == "":
            new_nodes.append(node)
            continue

        while current_text != "":
            links = extract(current_text)
            if len(links) == 0:
                new_nodes.append(TextNode(current_text, node.text_type, node.url))
                break

            alt, url = links[0]
            sections = current_text.split(f"{left_delimiter}{alt}{right_delimiter}{url_left}{url}{url_right}", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], node.text_type, node.url))

            new_nodes.append(TextNode(alt, text_type, url))
            current_text = sections[1]

    return new_nodes

