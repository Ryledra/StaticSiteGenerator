import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        children = []
        props = {}
        node = HTMLNode("p", "Hello World", children, props)
        self.assertRaises(NotImplementedError)

    def test_props_to_html(self):
        children = []
        props = {"href":"https://www.google.com",
                 "target":"_blank"}
        node = HTMLNode("p", "Hello World", children, props)
        expected_html = "href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(expected_html, node.props_to_html())

    def test_props_to_html_None(self):
        children = []
        node = HTMLNode("p", "Hello World", children)
        expected_html = ""
        self.assertEqual(expected_html, node.props_to_html())

if __name__ == "__main__":
    unittest.main()
