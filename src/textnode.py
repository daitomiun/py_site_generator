from enum import Enum

class TextNode():
    def __init__(self, text, text_type, url=""):
        self.text = text
        self.text_type = self.validate_text_type(text_type)
        self.url = url

    def __eq__(self, value) -> bool:
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def validate_text_type(self, text_type):
        if not isinstance(text_type, TextType):
            raise ValueError("ERR: text_type in the text node needs to be of TextType")
        return text_type

class TextType(Enum):
    BOLD = "bold"
    TEXT = "text"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

