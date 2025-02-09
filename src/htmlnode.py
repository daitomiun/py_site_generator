class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props != None and len(self.props) != 0:
            html_props = ""
            for prop in self.props:
                html_props += f'{prop}="{self.props[prop]}" '
            return " " + html_props.rstrip()
        return ""

