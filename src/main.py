from leafnode import LeafNode
from parentnode import ParentNode


def main():
    # 1st check
    node = ParentNode( "div", [LeafNode("p", "text")], {"class": "container", "id": "main"})
    print(f"RESULT: {node.to_html()}")
    print("---------------------------------")
main()
