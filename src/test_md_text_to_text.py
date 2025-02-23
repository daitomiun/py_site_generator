import unittest

from md_text_to_text import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
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

    def test_split_valid_nodes_by_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", 
                    TextType.LINK, 
                    "https://www.youtube.com/@bootdotdev"
                ),
                TextNode(" and", TextType.TEXT),
            ]
        )

    def test_split_invalid_and_valid_nodes_by_links(self):
        node = TextNode(
            "This is text with a link [to boot[] dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link [to boot[] dev](https://www.boot.dev) and " , TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
                TextNode(" and", TextType.TEXT),
            ]
        )

    def test_split_empty_node(self):
        node = TextNode("", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_multiple_input_nodes(self):
        nodes = [
            TextNode("Start [link](url) middle", TextType.TEXT),
            TextNode("Another [link2](url2) end", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Start " , TextType.TEXT),
                TextNode("link", TextType.LINK, "url"),
                TextNode(" middle", TextType.TEXT),
                TextNode("Another " , TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" end", TextType.TEXT)
            ]
        )

    def test_url_with_special_chars(self):
        node = TextNode("[link](https://example.com?param=value&other=123)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [TextNode("link", TextType.LINK, "https://example.com?param=value&other=123")]
        )
    def test_adjacent_links(self):
        node = TextNode("[link1](url1)[link2](url2)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [TextNode("link1", TextType.LINK, "url1"), TextNode("link2", TextType.LINK, "url2")]
        )
    def test_mixed_images_and_links(self):
        node = TextNode("![img](img_url)[link](link_url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [TextNode("![img](img_url)", TextType.TEXT), TextNode("link", TextType.LINK, "link_url")]
        )

    def test_split_valid_nodes_by_image(self):
        node = TextNode(
                "This is text with an image ![cute bear](https://example.com/bear.jpg) and some text after it",
                TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an image ", TextType.TEXT),
                TextNode("cute bear", TextType.IMAGE, "https://example.com/bear.jpg"),
                TextNode(" and some text after it", TextType.TEXT),
            ]
        )

    def test_split_invalid_and_valid_nodes_by_image(self):
        node = TextNode(
                "This is text with an image ![cute bear](https://example.com/bear.jpg ()) and some text after it![cute bear](https://example.com/bear.jpg)",
                TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an image ![cute bear](https://example.com/bear.jpg ()) and some text after it", TextType.TEXT, ), 
                TextNode("cute bear", TextType.IMAGE, "https://example.com/bear.jpg")
            ]
        )

    def test_valid_text_to_textnodes_with_links_images(self):
        md_text = "Check out these [cool pics](https://pics.com) and ![sunset](https://sunset.jpg) and [another](https://test.com/path?q=1) with a ![second image](https://img2.jpg)"
        result = text_to_textnodes(md_text)
        self.assertEqual(
            result,
            [
                TextNode("Check out these ", TextType.TEXT, ""),
                TextNode("cool pics", TextType.LINK, "https://pics.com"),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("sunset", TextType.IMAGE, "https://sunset.jpg"),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("another", TextType.LINK, "https://test.com/path?q=1"),
                TextNode(" with a ", TextType.TEXT, ""),
                TextNode("second image", TextType.IMAGE, "https://img2.jpg")
            ]
        )

    def test_valid_text_to_textnodes_with_mixed_code_links_images(self):
        md_text = "Here's some `inline code` followed by a [link with spaces](https://api.test.com/path with spaces) and a ![complex image](https://image.com/test.jpg?size=large&type=png) and `more code`"
        result = text_to_textnodes(md_text)
        self.assertEqual(
            result,
            [
                TextNode("Here's some ", TextType.TEXT, ""),
                TextNode("inline code", TextType.CODE, ""),
                TextNode(" followed by a ", TextType.TEXT, ""),
                TextNode("link with spaces", TextType.LINK, "https://api.test.com/path with spaces"),
                TextNode(" and a ", TextType.TEXT, ""),
                TextNode("complex image", TextType.IMAGE, "https://image.com/test.jpg?size=large&type=png"),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("more code", TextType.CODE, "")
            ]
        )
        pass

    def test_valid_text_to_textnodes_with_escaped_characters(self):
        md_text = "Test with `code & symbols` and [link & special chars](https://test.com/path?name=value&x=1) and ![image with spaces](https://api.test.com/img/1?title=sunny day&size=large) and *text with [escaped] characters*"
        result = text_to_textnodes(md_text)
        self.assertEqual(
            result,
            [
                TextNode("Test with ", TextType.TEXT, ""),
                TextNode("code & symbols", TextType.CODE, ""),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("link & special chars", TextType.LINK, "https://test.com/path?name=value&x=1"),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("image with spaces", TextType.IMAGE, "https://api.test.com/img/1?title=sunny day&size=large"),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode("text with [escaped] characters", TextType.ITALIC, "")
            ]
        )



    def test_valid_text_to_textnodes_with_mixed_quotes(self):
        md_text = """Testing "quoted" text with `code "containing" quotes` and [link "with" quotes](https://test.com/"quote"?q="hi") and ![image 'mixed' "quotes"](https://api.test.com/img?title="sunny's day") and *italic "with" quotes*"""
        result = text_to_textnodes(md_text)
        self.assertEqual(
            result,
            [
                TextNode('Testing "quoted" text with ', TextType.TEXT, ""),
                TextNode('code "containing" quotes', TextType.CODE, ""),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode('link "with" quotes', TextType.LINK, 'https://test.com/"quote"?q="hi"'),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode('image \'mixed\' "quotes"', TextType.IMAGE, 'https://api.test.com/img?title="sunny\'s day"'),
                TextNode(" and ", TextType.TEXT, ""),
                TextNode('italic "with" quotes', TextType.ITALIC, "")
            ]
        )
    def test_valid_text_to_textnodes_with_mixed_delimiters_spacing(self):
        md_text = "`code   with   spaces`[link with**bold**attempt](https://test.com)*italic  spaces  here*![image   spaces](https://img.com/test)`no spaces`**bold**[](empty link)![](empty image)"
        result = text_to_textnodes(md_text)
        self.assertEqual(
            result,
            [
                TextNode("", TextType.TEXT, ""),
                TextNode("code   with   spaces", TextType.CODE, ""),
                TextNode("[link with", TextType.TEXT, ""),
                TextNode("bold", TextType.BOLD, ""),
                TextNode("attempt](https://test.com)", TextType.TEXT, ""),
                TextNode("italic  spaces  here", TextType.ITALIC, ""),
                TextNode("image   spaces", TextType.IMAGE, "https://img.com/test"),
                TextNode("no spaces", TextType.CODE, ""),
                TextNode("bold", TextType.BOLD, ""),
                TextNode("", TextType.LINK, "empty link"),
                TextNode("", TextType.IMAGE, "empty image")
            ]
        )

if __name__ == "__main__":
    unittest.main()

