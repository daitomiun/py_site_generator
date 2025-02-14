

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # the delimiter checks and parses the information given
    # the text_type dictates the inner 1st level delimiter if it's code, bold, text, etc
    # old nodes are the nodes sent to use to split and delimit the markdown
    new_nodes = []
    for node in old_nodes:
        pos = 0
        while pos < len(node.text):
            print(repr(node))
            # Find first delimiter
            start = node.text.find(delimiter, pos)
            if start == -1:
                break
            # Find matching delimiter
            end = node.text.find(delimiter, start + len(delimiter))
            if end == -1:
                raise ValueError("Unclosed delimiter")
            # What should we do with this pair?
            pos = end + len(delimiter)

            # returns a list of text nodes

