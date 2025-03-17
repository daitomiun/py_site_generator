from md_text_to_text import split_nodes_link, text_to_textnodes
from md_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType

def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(markdown_to_blocks(md))

main()
