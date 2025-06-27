import unittest
import inspect
from src.handeler_text import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
'''  27 tests
class TextType(Enum):    
    TEXT = "text"       #"Normal text"
    BOLD = "bold"       #"**Bold text**"
    ITALIC = "italic"   #"_Italic text_"
    CODE = "code"       #"`Code text`"
    LINK = "link"       #"[anchor text](url)"
    IMAGE = "image"     #"![alt text](url)"
'''

#handeler text_node_to_html_node() 6 test
class TestTextNodeToHtmlNode(unittest.TestCase):
    #print("DEBUG: TestSplitNodesLink class loaded")
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

    def test_plain_text_makes_leafnode_with_no_tag(self):
        text_node = TextNode("Just text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Just text")



#handeler split_nodes_delimiter() 4 test
class Test_split_nodes_delimiter(unittest.TestCase):
    #print("DEBUG: Test_split_nodes_delimiter class loaded")
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

    def test_italic_issue_with_code(self):
        test=[TextNode("This is a **simple paragraph** to start things off. It also has some _italic_ text and a piece of ```codesnippet()```.", TextType.TEXT)]
        result=split_nodes_delimiter(test,"_", TextType.ITALIC)
        expected=[
            TextNode('This is a **simple paragraph** to start things off. It also has some ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(" text and a piece of ```codesnippet()```.",TextType.TEXT),
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
        #BOLD
        result=split_nodes_delimiter(node,"**", TextType.BOLD)
        expected=[TextNode('Alpha `code` Omega', TextType.TEXT), TextNode('Bolded phrase', TextType.BOLD), TextNode(' at start.', TextType.TEXT), TextNode('A little _italic_ sprinkled in.', TextType.TEXT), TextNode('Plain beginning then ', TextType.TEXT), TextNode('bold', TextType.BOLD), TextNode('.', TextType.TEXT), TextNode('Multiple `bits` of `code` blocks.', TextType.TEXT), TextNode('_Italics_ everywhere _here_!', TextType.TEXT), TextNode('Ends with bold ', TextType.TEXT), TextNode('emphasis', TextType.BOLD), TextNode('No formatting present at all.', TextType.TEXT), TextNode('Edge at start: `begin` middle end.', TextType.TEXT), TextNode('At the end comes _finale_', TextType.TEXT)]
        self.assertEqual(result,expected)
        #CODE
        result=split_nodes_delimiter(node,"`", TextType.CODE)
        expected=[TextNode('Alpha ', TextType.TEXT), TextNode('code', TextType.CODE), TextNode(' Omega', TextType.TEXT), TextNode('**Bolded phrase** at start.', TextType.TEXT), TextNode('A little _italic_ sprinkled in.', TextType.TEXT), TextNode('Plain beginning then **bold**.', TextType.TEXT), TextNode('Multiple ', TextType.TEXT), TextNode('bits', TextType.CODE), TextNode(' of ', TextType.TEXT), TextNode('code', TextType.CODE), TextNode(' blocks.', TextType.TEXT), TextNode('_Italics_ everywhere _here_!', TextType.TEXT), TextNode('Ends with bold **emphasis**', TextType.TEXT), TextNode('No formatting present at all.', TextType.TEXT), TextNode('Edge at start: ', TextType.TEXT), TextNode('begin', TextType.CODE), TextNode(' middle end.', TextType.TEXT), TextNode('At the end comes _finale_', TextType.TEXT)]
        self.assertEqual(result,expected)
        #ITALIC
        result=split_nodes_delimiter(node,"_", TextType.ITALIC)
        expected=[TextNode('Alpha `code` Omega', TextType.TEXT), TextNode('**Bolded phrase** at start.', TextType.TEXT), TextNode('A little ', TextType.TEXT), TextNode('italic', TextType.ITALIC), TextNode(' sprinkled in.', TextType.TEXT), TextNode('Plain beginning then **bold**.', TextType.TEXT), TextNode('Multiple `bits` of `code` blocks.', TextType.TEXT), TextNode('Italics', TextType.ITALIC), TextNode(' everywhere ', TextType.TEXT), TextNode('here', TextType.ITALIC), TextNode('!', TextType.TEXT), TextNode('Ends with bold **emphasis**', TextType.TEXT), TextNode('No formatting present at all.', TextType.TEXT), TextNode('Edge at start: `begin` middle end.', TextType.TEXT), TextNode('At the end comes ', TextType.TEXT), TextNode('finale', TextType.ITALIC)]
        self.assertEqual(result,expected)

#test extract_markdown_images() 1 test
class test_extract_markdown_images(unittest.TestCase):
    #print("DEBUG: test_extract_markdown_images class loaded")
    #handeler function extract_markdown_images()
    def test_largetext_with_imbigue(self):
        text = "This is text with a " \
            "![rick roll](https://i.imgur.com/aK.gif)" \
            " and ![obi wan](https://i.imgur.com/Vk.jpeg)" \
            " and ![abi (https://i.jpeg)" \
            " and ![q](https://i."
        
        # Only expect the 2 valid matches!
        expected = [
            ('rick roll', 'https://i.imgur.com/aK.gif'), 
            ('obi wan', 'https://i.imgur.com/Vk.jpeg')
        ]
        result = extract_markdown_images(text)
        self.assertEqual(expected, result)

#test extract_markdown_links() 2 test
class test_extract_markdown_links(unittest.TestCase):
    #print("DEBUG: test_extract_markdown_links class loaded")
    def test_simple_links(self):
        simple_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"
        result=extract_markdown_links(simple_text)
        expected=[('to boot dev', 'https://www.boot.dev')]
        self.assertEqual(expected, result)
    
    def test_complex_links(self):
        large_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) " \
            "[rick roll](https://i.imgur.com/aKaOqIh.gif)" \
            " and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" \
            " and [abi (https://i.jpeg)" \
            ""
        result=extract_markdown_links(large_text)
        expected=[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev'), ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(expected, result)

#test split_nodes_image() 7 test
class test_split_nodes_image(unittest.TestCase):
    #print("DEBUG: test_split_nodes_image class loaded")
    def test_simple_test(self):
        simple_text = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        result=split_nodes_image([simple_text])
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode(' and ', TextType.TEXT), 
                  TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
                  ]
        self.assertEqual(expected, result)


    def test_complex_test(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) " \
            "![rick roll](https://i.imgur.com/aKaOqIh.gif)" \
            " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" \
            " and ![abi (https://i.jpeg)", \
            TextType.TEXT)        
        result=split_nodes_image([node])
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode(' and ', TextType.TEXT), 
                 TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev'), 
                 TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'), 
                 TextNode(' and ', TextType.TEXT), 
                 TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'), 
                 TextNode(' and ![abi (https://i.jpeg)', TextType.TEXT)
                 ]
        self.assertEqual(expected, result)
    
    def test_invalid_node_type(self):
        # Pass in something that's not a TextNode
        invalid_nodes = ["not a TextNode", 123, None]
        with self.assertRaises(ValueError):
            split_nodes_image(invalid_nodes)

    

    def test_raises_on_none(self):
        with self.assertRaises(ValueError):
            split_nodes_image(None)

    def test_invalid_node_type2(self):
        invalid_nodes = [ ]
        self.assertRaises(ValueError, split_nodes_image, invalid_nodes)
    def test_invalid_node_type3(self):
        invalid_nodes = ""
        self.assertRaises(ValueError, split_nodes_image, invalid_nodes)

    def test_complex_list_nodes(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node2 = TextNode("[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node3 = TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node4 = TextNode("[to boot dev](https://www.boot.dev)This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node5 = TextNode("", TextType.TEXT)        
        node6 = TextNode("This is text [to boot dev](https://www.boot.dev) with a link ", TextType.TEXT)        
        node7 = TextNode("[to boot dev](https://www.boot.dev) This is text with a link ", TextType.TEXT)   
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode('This is text ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode(' with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), 
                  TextNode(' This is text with a link ', TextType.TEXT)]
        result=split_nodes_link([node,node2,node3,node4,node5,node6,node7])
        self.assertListEqual(expected, result)


#test split_nodes_link() 7 tests
class test_split_nodes_link(unittest.TestCase):
    #print("DEBUG: test_split_nodes_link class loaded")
    def test_simple_test(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        result=split_nodes_image([node])
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode(' and ', TextType.TEXT), 
                  TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
                  ]
        self.assertListEqual(expected, result)

    def test_complex_test(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) " \
            "![rick roll](https://i.imgur.com/aKaOqIh.gif)" \
            " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" \
            " and ![abi (https://i.jpeg)", \
            TextType.TEXT)  
        result=split_nodes_image([node])
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                TextNode(' and ', TextType.TEXT), 
                TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev'), 
                TextNode('rick roll', TextType.IMAGE, 'https://i.imgur.com/aKaOqIh.gif'), 
                TextNode(' and ', TextType.TEXT), 
                TextNode('obi wan', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'), 
                TextNode(' and ![abi (https://i.jpeg)', TextType.TEXT)]
        self.assertListEqual(expected, result)

    def test_invalid_node_type(self):
        # Pass in something that's not a TextNode
        invalid_nodes = ["not a TextNode", 123, None]
        with self.assertRaises(ValueError):
            split_nodes_image(invalid_nodes)
    

    def test_raises_on_none(self):
        with self.assertRaises(ValueError):
            split_nodes_image(None)

    def test_invalid_node_type2(self):
        invalid_nodes = [ ]
        self.assertRaises(ValueError, split_nodes_image, invalid_nodes)
    def test_invalid_node_type3(self):
        invalid_nodes = ""
        self.assertRaises(ValueError, split_nodes_image, invalid_nodes)

    def test_complex_list_nodes(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node2 = TextNode("![to boot dev](https://www.boot.dev)![to boot dev](https://www.boot.dev)![to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node3 = TextNode("![to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node4 = TextNode("![to boot dev](https://www.boot.dev)This is text with a link ![to boot dev](https://www.boot.dev)", TextType.TEXT)        
        node5 = TextNode("", TextType.TEXT)        
        node6 = TextNode("This is text ![to boot dev](https://www.boot.dev) with a link ", TextType.TEXT)        
        node7 = TextNode("![to boot dev](https://www.boot.dev) This is text with a link ", TextType.TEXT)   
        expected=[TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('This is text with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode('This is text ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode(' with a link ', TextType.TEXT), 
                  TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'), 
                  TextNode(' This is text with a link ', TextType.TEXT)]
        result=split_nodes_image([node,node2,node3,node4,node5,node6,node7])
        self.assertListEqual(expected, result)

#test text_to_textnodes(text) 7 tests
class test_text_to_textnodes(unittest.TestCase):
    def test_simple_text(self):
        text="This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result=text_to_textnodes(text)
        expected=[TextNode('This is ', TextType.TEXT),
            TextNode('text', TextType.BOLD), 
            TextNode(' with an ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC), 
            TextNode(' word and a ', TextType.TEXT), 
            TextNode('code block', TextType.CODE), 
            TextNode(' and an !', TextType.TEXT), 
            TextNode('obi wan image', TextType.LINK, 'https://i.imgur.com/fJRm4Vk.jpeg'), 
            TextNode(' and a ', TextType.TEXT), 
            TextNode('link', TextType.LINK, 'https://boot.dev')]
        self.assertListEqual(expected, result)

    def test_simple_text_2types(self):
            text = "**bold**_italic_"
            result=text_to_textnodes(text)
            expected=[TextNode('bold', TextType.BOLD), TextNode('italic', TextType.ITALIC)]
            self.assertListEqual(expected, result)
        

    def test_valueerrors(self):
        invalid_nodes = TextNode(' and a ', TextType.TEXT)
        with self.assertRaises(ValueError):
            text_to_textnodes(invalid_nodes)

    def test_empty_string_raises_error(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("")

    def test_list_raises_error(self):
        with self.assertRaises(ValueError):
            text_to_textnodes(["anything"])
    
    def test_int_raises_error(self):
        with self.assertRaises(ValueError):
            text_to_textnodes(123)
    def test_None_raises_error(self):
        with self.assertRaises(ValueError):
            text_to_textnodes(None)

