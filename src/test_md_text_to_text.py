import unittest

from md_text_to_text import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from textnode import TextNode, TextType

class TestMDTextToTextNode(unittest.TestCase):
    def test_invalid_delimiter(self):
        with self.assertRaisesRegex(ValueError, "Invalid empty delimeter"):
            code_node = TextNode("Here is `some code` and more code", TextType.TEXT)
            split_nodes_delimiter([code_node], "", TextType.CODE)

    def test_unclosed_delimeter(self):
        with self.assertRaisesRegex(ValueError, "Unclosed delimiter"):
            code_node = TextNode("Here is `some code` and `more code", TextType.TEXT)
            split_nodes_delimiter([code_node], "`", TextType.CODE)

    def test_valid_italic_delimeter(self):
        italic_node = TextNode("Here is *italic text* and *more italic*", TextType.TEXT)
        result = split_nodes_delimiter([italic_node], "*", TextType.ITALIC)
 
        self.assertEqual(result[0].text, "Here is ")
        self.assertEqual(result[1].text, "italic text")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "more italic")
        self.assertEqual(result[3].text_type, TextType.ITALIC)
        self.assertEqual(len(result), 4)

    def test_valid_bold_delimeter(self):
        bold_node = TextNode("**Bold** at start and **Bold** at **end**", TextType.TEXT)
        result = split_nodes_delimiter([bold_node], '**', TextType.BOLD)

        self.assertEqual(result[0].text, "")
        self.assertEqual(result[1].text, "Bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " at start and ")
        self.assertEqual(result[3].text, "Bold")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " at ")
        self.assertEqual(result[5].text, "end")
        self.assertEqual(result[5].text_type, TextType.BOLD)
        self.assertEqual(len(result), 6)

    def test_valid_code_delimeter(self):
        code_node = TextNode("Here is `some code` and `more code`", TextType.TEXT)
        result = split_nodes_delimiter([code_node], "`", TextType.CODE)

        self.assertEqual(result[0].text, "Here is ")
        self.assertEqual(result[1].text, "some code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "more code")
        self.assertEqual(result[3].text_type, TextType.CODE)
        self.assertEqual(len(result), 4)

    def test_valid_empty_delimeter(self):
        bold_emtpy_node = TextNode("Empty **** delimiters", TextType.TEXT)
        result = split_nodes_delimiter([bold_emtpy_node], "**", TextType.BOLD)

        self.assertEqual(result[0].text, "Empty ")
        self.assertEqual(result[1].text, "")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " delimiters")
        self.assertEqual(len(result), 3)

    def test_valid_non_text_node(self):
        mixed_nodes = [
            TextNode("Here is **bold** text", TextType.TEXT),
            TextNode("This is untouched node", TextType.BOLD)
        ]
        result = split_nodes_delimiter(mixed_nodes, "**", TextType.BOLD)

        self.assertEqual(result[0].text, "Here is ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[3].text, "This is untouched node")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(len(result), 4)

    def test_valid_overlaping_delimiters(self):
        mixed_nodes = [ TextNode("This is ****bold**** text", TextType.TEXT) ] 
        result = split_nodes_delimiter(mixed_nodes, "**", TextType.BOLD)

        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[1].text, "")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, "bold")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "")
        self.assertEqual(result[3].text_type, TextType.BOLD)
        self.assertEqual(result[4].text, " text")
        self.assertEqual(len(result), 5)

    def test_valid_markdown_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)

        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(len(result), 2)

    def test_invalid_markdown_image_brackets_extraction(self):
        text = "This is text with a ![rick [] roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)

        self.assertEqual(result, [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(len(result), 1)

    def test_invalid_markdown_image_parenthesis_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif ()) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)

        self.assertEqual(result, [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(len(result), 1)

    def test_valid_markdown_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(result, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(len(result), 2)

    def test_invalid_markdown_brackets_link_extraction(self):
        text = "This is text with a link [to boot [hello] dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(result, [('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(len(result), 1)

    def test_invalid_markdown_link_parenthesis_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev ()) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(result, [('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(len(result), 1)

if __name__ == "__main__":
    unittest.main()

