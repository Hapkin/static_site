import unittest
from src.parentnode import ParentNode
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
        
        node2 = LeafNode("p", "Test", props={"style":"color:green"})
        node3 = LeafNode("li","my text")
        node4 = ParentNode("lo", [node3])
        
        node1 = ParentNode("a",[node2, node4], {"href":"https://www.google.be","target":"_blanc"})
        
        
        self.assertEqual(type(node1.tag), str)
        self.assertEqual(type(node1.children), list)
        self.assertIsInstance(node1.children[0], LeafNode) #(HTMLNode,ParentNode,LeafNode))
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


    def test_properties(self):        
        node = ParentNode("p", children=[LeafNode("b", "Bold text")], props={"style":"color:green"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, [LeafNode("b", "Bold text")])
        self.assertDictEqual(node.props, {"style": "color:green"})

        node2 = ParentNode("a",children=[node], props={"href":"https://www.google.be","target":"_blanc"})
        self.assertEqual(node2.tag, "a")
        self.assertEqual(node2.children, [node])
        self.assertDictEqual(node2.props, {"href":"https://www.google.be","target":"_blanc"})

        node3 = ParentNode("a",children=[node2], props={"href":"https://www.google.be","target":"_new"})
        self.assertEqual(type(node3.children), list)

    
    def test_to_html(self):
        node = ParentNode("p", children=[LeafNode("b", "Bold text")], props={"style":"color:green"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, [LeafNode("b", "Bold text")])
        self.assertEqual(node.to_html(),'<p style="color:green"><b>Bold text</b></p>')

        node2 = ParentNode("h1",children=[node], props={"href":"https://www.google.be","target":"_blanc"})
        self.assertEqual(node2.tag, "h1")
        self.assertEqual(node2.children, [node])
        self.assertEqual(node2.props, {"href":"https://www.google.be","target":"_blanc"})
        self.assertEqual(node2.to_html(),'<h1 href="https://www.google.be" target="_blanc"><p style="color:green"><b>Bold text</b></p></h1>')

        node3 = ParentNode("a",children=[node2], props={"href":"https://www.google.be","target":"_new"})
        self.assertEqual(type(node3.children), list)
        self.assertEqual(node3.to_html(),'<a href="https://www.google.be" target="_new"><h1 href="https://www.google.be" target="_blanc"><p style="color:green"><b>Bold text</b></p></h1></a>')

    def test_to_html_raises_missing_tag(self):
        node = ParentNode(None, [LeafNode("em", "text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_children_list(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()
    
    def test_invalid_children_type(self):
        node=ParentNode("div", LeafNode("b", "Bold text"))  # Not in a list
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raises_missing_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raises_empty_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_children_must_be_list(self):
        node = ParentNode("ul", LeafNode("li", "not in a list"))
        with self.assertRaises(ValueError):
            node.to_html()

    def test_props_render_to_html(self):
        node = ParentNode("a", [LeafNode(None, "click me")], props={"href": "boot.dev"})
        html = node.to_html()
        self.assertIn('href="boot.dev"', html)
        self.assertTrue(html.startswith("<a "))



if __name__ == "__main__":
    unittest.main(verbosity=2)