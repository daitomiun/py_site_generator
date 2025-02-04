from htmlnode import HTMLNode 

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return self.value

        props = self.props_to_html()
        return f'<{self.tag} {props}>{self.value}</{self.tag}>'

