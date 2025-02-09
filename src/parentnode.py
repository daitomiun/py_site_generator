from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ERR: The parent Node needs a tag value")
        if self.children is None or len(self.children) == 0 or not isinstance(self.children, list):
            raise ValueError("ERR: The parent Node needs a valid children value")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("ERR: All children must be HTMLNode objects")
            html += child.to_html()
        html += f"</{self.tag}>"
        return html

