from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: raise ValueError
        if self.tag is None: return self.value
        if self.props is None: return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{" ".join([self.tag, self.props_to_html()])}>{self.value}</{self.tag}>"

if __name__ == "__main__":
    node1 = LeafNode("This is a paragraph of text.", "p")
    node2 = LeafNode("Click me!", "a", {"href": "https://www.google.com"})

    print(node1)
    print(node1.to_html())
    print(node2)
    print(node2.to_html())
