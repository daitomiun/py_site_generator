from md_text_to_text import split_nodes_link
from textnode import TextNode, TextType

def main():
    node = TextNode("![img](img_url)[link](link_url)", TextType.TEXT)
    print(split_nodes_link([node]))
main()
