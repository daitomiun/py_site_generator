from md_text_to_text import split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

def main():
    node = TextNode("![img](img_url)[link](link_url)", TextType.TEXT)
    print(split_nodes_link([node]))

    print("0. ---------------------------------------------")
    md_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    print("1. ---------------------------------------------")
    '''
    md_text = "This is *italic with **bold** inside* and **bold with *italic* inside**"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    print("2. ---------------------------------------------")
    md_text = "Check out these [cool pics](https://pics.com) and ![sunset](https://sunset.jpg) and [another](https://test.com/path?q=1) with a ![second image](https://img2.jpg)"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    print("3. ---------------------------------------------")
    md_text = "`code with *italic* attempt` and *italic with `code` attempt* and **bold with ![image](url) inside**"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    print("4. ---------------------------------------------")
    md_text = "This has an [unclosed link and a *missing delimiter"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    '''
    print("5. ---------------------------------------------")
    md_text = "Check out these [cool pics](https://pics.com) and ![sunset](https://sunset.jpg) and [another](https://test.com/path?q=1) with a ![second image](https://img2.jpg)"
    print(md_text)
    nodes = text_to_textnodes(md_text)
    print(nodes)
    print("5. ---------------------------------------------")
main()
