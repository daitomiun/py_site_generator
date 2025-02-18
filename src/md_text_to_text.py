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

