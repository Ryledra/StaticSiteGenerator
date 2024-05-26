from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: raise ValueError
        if self.tag is None: return self.value
        return f"<{self.tag}{" " if self.props is not None else ""
                }{self.props_to_html()}>{self.value}</{self.tag}>"

if __name__ == "__main__":
    node1 = LeafNode("p", "This is a paragraph of text.")
    node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(node1.to_html())
    print(node2.to_html())
