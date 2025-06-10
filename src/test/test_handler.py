import unittest
from src.handeler import text_node_to_html_node
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
'''
class TextType(Enum):    
    TEXT = "text"       #"Normal text"
    BOLD = "bold"       #"**Bold text**"
    ITALIC = "italic"   #"_Italic text_"
    CODE = "code"       #"`Code text`"
    LINK = "link"       #"[anchor text](url)"
    IMAGE = "image"     #"![alt text](url)"
'''


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_valid_text_type_returns_leafnode(self):
        text_node = TextNode("Bold bears!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold bears!")

    def test_valid_text_type_returns_leafnode_italic(self):
        text_node = TextNode("Italic bears!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic bears!")

    def test_valid_text_type_returns_leafnode_code(self):
        text_node = TextNode("print('bears!')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('bears!')")

#return LeafNode("img", value="", props={"src":text_node.url, "alt":text_node.text})
    def test_valid_text_type_returns_leafnode_img(self):
        text_node = TextNode("lame picture", TextType.IMAGE,  "www.google.be")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertDictEqual(html_node.props, {"src":"www.google.be", "alt":"lame picture"})

#return LeafNode("a", value=text_node.text, props={"href":text_node.url})
    def test_valid_text_type_returns_leafnode_link(self):
        text_node = TextNode("Go bears!", TextType.LINK, "http://whatever.com")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Go bears!")
        self.assertDictEqual(html_node.props, {"href":"http://whatever.com"})

    def test_invalid_text_type_raises(self):
        class FakeType:
            pass
        text_node = TextNode("Mystery", FakeType())
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(text_node)
        self.assertIn("is not a valid TextType", str(context.exception))

    def test_plain_text_makes_leafnode_with_no_tag(self):
        text_node = TextNode("Just text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Just text")

