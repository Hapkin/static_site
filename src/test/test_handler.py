import unittest
from src.handeler import text_node_to_html_node, split_nodes_delimiter
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

#handeler function
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



#handeler function
class Test_split_nodes_delimiter(unittest.TestCase):
    def test_bold_locations(self):    
        test=[
            TextNode("**start** bold text",TextType.TEXT),
            TextNode("why so serious **END**",TextType.TEXT),
            TextNode("how about **the middle** of the sentence",TextType.TEXT),
        ]
        result=split_nodes_delimiter(test,"**",TextType.BOLD)
        expected=[
            TextNode('start', TextType.BOLD), 
            TextNode(' bold text', TextType.TEXT), 
            TextNode('why so serious ', TextType.TEXT), 
            TextNode('END', TextType.BOLD), 
            TextNode('how about ', TextType.TEXT), 
            TextNode('the middle', TextType.BOLD), 
            TextNode(' of the sentence', TextType.TEXT)
            ]
        self.assertEqual(result,expected)

    def test_italic_multiple(self):    
        test=[
            TextNode("_start_ bold _text_",TextType.TEXT),
            TextNode("why _so_ _serious_ **END**",TextType.TEXT),
        ]
        result=split_nodes_delimiter(test,"_", TextType.ITALIC)
        expected=[
            TextNode('start', TextType.ITALIC),
            TextNode(' bold ', TextType.TEXT), 
            TextNode('text', TextType.ITALIC), 
            TextNode('why ', TextType.TEXT), 
            TextNode('so', TextType.ITALIC), 
            TextNode(' ', TextType.TEXT), 
            TextNode('serious', TextType.ITALIC), 
            TextNode(' **END**', TextType.TEXT)
            ]
        self.assertEqual(result,expected)
        
    def test_bold_multiples(self):
        test=[ TextNode( '**This** is text with a **bolded phrase** in the middle', TextType.TEXT)] 
        result=split_nodes_delimiter(test,"**", TextType.BOLD)
        expected = [
            TextNode('This', TextType.BOLD),
            TextNode(' is text with a ', TextType.TEXT),
            TextNode('bolded phrase', TextType.BOLD),
            TextNode(' in the middle', TextType.TEXT)
            ]
        self.assertEqual(result,expected)
'''
    def test_multinodes(self):
        node=[
            TextNode("Alpha `code` Omega", TextType.TEXT),
            TextNode("**Bolded phrase** at start.", TextType.TEXT),
            TextNode("A little _italic_ sprinkled in.", TextType.TEXT),
            TextNode("Plain beginning then **bold**.", TextType.TEXT),
            TextNode("Multiple `bits` of `code` blocks.", TextType.TEXT),
            TextNode("_Italics_ everywhere _here_!", TextType.TEXT),
            TextNode("Ends with bold **emphasis**", TextType.TEXT),
            TextNode("No formatting present at all.", TextType.TEXT),
            TextNode("Edge at start: `begin` middle end.", TextType.TEXT),
            TextNode("At the end comes _finale_", TextType.TEXT),
        ]
'''