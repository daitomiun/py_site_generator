
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props != None:
            html_props = ""
            for prop in self.props:
                html_props += f'{prop}="{self.props[prop]}" '
            return " " + html_props.rstrip()
        return ""

