import unittest

from md_to_blocks import BlockType, block_to_block_type, markdown_to_blocks

class TestMDToBlocksNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "Just one paragraph with no blank lines."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one paragraph with no blank lines."])

    def test_excessive_whitespace(self):
        md = "First block\n\n\n\nSecond block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_different_block_types(self):
        md = "# Heading\n\nParagraph\n\n```\ncode block\n```"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# Heading", "Paragraph", "```\ncode block\n```"])

    def test_leading_trailing_newlines(self):
        md = "\n\nMiddle block\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Middle block"])

    def test_paragraph(self):
        block = "This is a simple paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = "This is a paragraph\nwith multiple lines\nbut no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# Level 1 Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "###### Level 6 Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "#NoSpaceHeading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = "```python\ndef hello():\n    print('Hello world')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = "> Line 1\nLine 2\n> Line 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
