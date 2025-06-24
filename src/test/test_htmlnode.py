import unittest
import inspect
from src.leafnode import LeafNode, ParentNode

### ABSTRACT CLASS so you need to use children to perform tests...
# 2 test

class TestHtmlNodeStrRepr2(unittest.TestCase):
    #print("DEBUG: TestHtmlNodeStrRepr2 class loaded")
    def test_leafnode_str_repr(self):
        leaf = LeafNode(tag="span", value="Leaf", props={})
        # Ensure str and repr do not throw RecursionError (or anything)
        try:
            s = str(leaf)
            r = repr(leaf)
        except RecursionError:
            self.fail("RecursionError in __str__ or __repr__ with LeafNode")
        except Exception as e:
            self.fail(f"Unexpected error in __str__ or __repr__: {e}")
        self.assertIsInstance(s, str)
        self.assertIsInstance(r, str)
    
    def test_parentnode_str_repr(self):

        child = LeafNode(tag="span", value="Child", props={})
        parent = ParentNode(tag="div", children=[child], props={})
        
        try:
            s = str(parent)
            r = repr(parent)
        except RecursionError:
            self.fail("RecursionError in __str__ or __repr__ with ParentNode")
        except Exception as e:
            self.fail(f"Unexpected error in __str__ or __repr__: {e}")
        self.assertIsInstance(s, str)
        self.assertIsInstance(r, str)
''' 
BECAME OBSOLETE AS HTMLNODE IS NOW ABSTRACT
no instance of HTMLNode can be created


import unittest
from src.htmlnode import HTMLNode
 ##INFO##
    def __init__(self, tag=None, value=None, children=None,props=None):
        self.tag=tag                #string <a>
        self.value=value            #string the text inside a <p>paragraph</p>
        self.children=children    #list of HTMLNode []
        self.props=props            #dictionary {"href": "www.google.com"}


class TestHTMLNode(unittest.TestCase):
    def test_properties_types(self):
        node1 = HTMLNode("a","my_url",children=None, props={"href":"https://www.google.be","target":"_blanc"})
        node2 = HTMLNode("p", "Test", props={"style":"color:green"})
        childnodes= [node2]
        node1.children=childnodes
        
        self.assertEqual(type(node1.tag), str)
        self.assertEqual(type(node1.value), str)
        self.assertEqual(type(node1.children), list)
        self.assertEqual(type(node1.children[0]), HTMLNode)
        self.assertEqual(type(node1.props), dict)

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
'''