import unittest
from src.parentnode import ParentNode
from src.htmlnode import HTMLNode
from src.leafnode import LeafNode
''' ##INFO##
    def __init__(self, tag=None, value=None, children=None,props=None):
        self.tag=tag                #string <a>
        self.value=value            #string the text inside a <p>paragraph</p>
        self.children=children    #list of HTMLNode []
        self.props=props            #dictionary {"href": "www.google.com"}
'''

class TestParentNode(unittest.TestCase):
    def test_properties_types(self):
        
        node2 = HTMLNode("p", "Test", props={"style":"color:green"})
        node3 = HTMLNode("li","my text")
        node4 = ParentNode("lo", [node3])
        
        node1 = ParentNode("a",[node2, node4], {"href":"https://www.google.be","target":"_blanc"})
        
        
        self.assertEqual(type(node1.tag), str)
        self.assertEqual(type(node1.children), list)
        self.assertIsInstance(node1.children[0], HTMLNode) #(HTMLNode,ParentNode,LeafNode))
        self.assertEqual(type(node1.props), dict)


########not working yet

    def test_L5parentNode(self):
        node = ParentNode(
                "p",
                [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
            )

        print_test=node.to_html()
        self.assertEqual(print_test, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

##########todo update to ParentNodes
    def test_properties(self):        
        #node=HTMLNode(value="test")
        node = HTMLNode("p", "Test", props={"style":"color:green"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Test")
        self.assertEqual(node.children, None)
        self.assertDictEqual(node.props, {"style": "color:green"})

        node2 = HTMLNode("a","my_url",children=None, props={"href":"https://www.google.be","target":"_blanc"})
        self.assertEqual(node2.tag, "a")
        self.assertEqual(node2.value, "my_url")
        self.assertEqual(node2.children, None)
        self.assertDictEqual(node2.props, {"href":"https://www.google.be","target":"_blanc"})

        node3 = HTMLNode(value="only text")
        self.assertEqual(node3.value, "only text")
    
    def test_props_to_html(self):
        node = HTMLNode("a","my_url",props={"href":"https://www.google.be"})
        node2 = HTMLNode("a","my_url",props={"href":"https://www.google.be"})
        #print(f"1-->{str(node)}")     
        self.assertEqual(str(node),str(node2))

    def test_reprint(self):
        node = HTMLNode('a','my_url',props={'href':'https://www.google.be','target':'_blanc'})
        excepted= "HTML: <a>\ntext-inside: 'my_url'\nProps:\n'href': 'https://www.google.be', 'target': '_blanc'"
        self.assertEqual(repr(node),excepted)
 
          
    def test_emptyHTMLNode(self):
        node=HTMLNode()
        node2=HTMLNode()
        self.assertEqual(node,node2)
        
    def test_html_node_equality_different_tags(self):
        node1 = HTMLNode("p", "text")
        node2 = HTMLNode("div", "text")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main(verbosity=2)