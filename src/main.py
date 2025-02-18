from leafnode import LeafNode
from md_text_to_text import split_nodes_delimiter
from parentnode import ParentNode
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def main():
    # 1st check
    '''
    node = ParentNode( "div", [LeafNode("p", "text")], {"class": "container", "id": "main"})
    print(f"RESULT: {node.to_html()}")
    print("---------------------------------")
    text_node = TextNode("hello", TextType.BOLD)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("hello", TextType.ITALIC)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("hello", TextType.TEXT)
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    text_node = TextNode("print(hello)", TextType.CODE)
    print(repr(text_node_to_html_node(text_node)))
    text_node = TextNode("hello", TextType.LINK, "https://www.boot.dev")
    print("---------------------------------")
    print(repr(text_node_to_html_node(text_node)))
    text_node = TextNode("hello", TextType.IMAGE, "https://www.example.com/image.png")
    print(repr(text_node_to_html_node(text_node)))
    print("---------------------------------")
    test_node = TextNode("**Bold** at start and **Bold** at **end**", TextType.TEXT)
    print(split_nodes_delimiter([test_node], '**', TextType.BOLD))

    test_node = TextNode("Empty **** delimiters", TextType.TEXT)
    print(split_nodes_delimiter([test_node], '**', TextType.BOLD))
    # Test code blocks with backticks
    code_node = TextNode("Here is `some code` and `more code`", TextType.TEXT)
    code_result = split_nodes_delimiter([code_node], "`", TextType.CODE)
    print(code_result)

    # Test italics with single asterisk
    italic_node = TextNode("Here is *italic text* and *more italic*", TextType.TEXT)
    italic_result = split_nodes_delimiter([italic_node], "*", TextType.ITALIC)
    print(italic_result)

    # Test empty delimiter (should raise error)
    try:
        bad_result = split_nodes_delimiter([code_node], "", TextType.CODE)
    except ValueError as e:
        print(f"Correctly caught error: {e}")
    bold_node = TextNode("**Bold** at start and **Bold** at **end**", TextType.TEXT)
    print(split_nodes_delimiter([bold_node], '**', TextType.BOLD))
    '''
    mixed_nodes = [
        TextNode("Here is **bold** text", TextType.TEXT),
        TextNode("This is untouched node", TextType.BOLD)  # Non-TextType node
    ]

    result = split_nodes_delimiter(mixed_nodes, "**", TextType.BOLD)

    # Expected outcome:
    # The bold node ("This is untouched node") should remain the same and
    # unaffected by splitting logic. Meanwhile, the text node should split and
    # parse the bold content.
    print(result)

    test_node = TextNode("This is ****bold**** text", TextType.TEXT)

    result = split_nodes_delimiter([test_node], "**", TextType.BOLD)

    # Expected:
    # Node split should treat `****bold****` as a **single bold section** for "bold",
    # while interpreting the outer parts of the string as normal text.
    # New nodes:
    # - TextNode("This is ", TextType.TEXT)
    # - TextNode("", TextType.BOLD)      # Empty before bold content
    # - TextNode("bold", TextType.BOLD)
    # - TextNode("", TextType.BOLD)      # Empty after bold content
    # - TextNode(" text", TextType.TEXT)

    print(result)


main()
