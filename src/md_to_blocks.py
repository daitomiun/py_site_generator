from enum import Enum
import re

def markdown_to_blocks(markdown):
    markdown_strip = markdown.strip()
    markdown_split = [block.strip() for block in markdown_strip.split("\n\n") if block]
    return markdown_split

def block_to_block_type(block: str):
    if re.match("^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if starts_with_valid_block(block, "> "):
        print(f"quote: {block}")
        return BlockType.QUOTE
    if starts_with_valid_block(block, "- "):
        return BlockType.UNORDERED_LIST
    if validate_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def validate_ordered_list(block):
    lines = block.split('\n')
    for i, line in enumerate(lines):
        if not re.match(f"^{i+1}\\. ", line):
            return False
    return True

def starts_with_valid_block(block, delimeter):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith(delimeter.strip()):
            return False
    return True

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

