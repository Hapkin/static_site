import unittest
from src.leafnode import LeafNode
''' ##INFO##
    def __init__(self,tag,value, props=None):
        if (value is not None):
            super().__init__(tag, value, props)
        else:
            raise ValueError("LeafNode must have a value.")
'''
class TestLeafNode(unittest.TestCase):
    def test_properties_types(self):
        node1 = LeafNode("a","my_url",children=None, props={"href":"https://www.google.be","target":"_blanc"})
        node2 = LeafNode("p", "Test", props={"style":"color:green"})
        childnodes= [node2]
        node1.children=childnodes
        
        self.assertEqual(type(node1.tag), str)
        self.assertEqual(type(node1.value), str)
        self.assertEqual(type(node1.children), list)
        self.assertEqual(type(node1.children[0]), LeafNode)
        self.assertEqual(type(node1.props), dict)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "text")
        self.assertEqual(node.to_html(), "<p>text</p>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "print('text'")
        self.assertEqual(node.to_html(), "<code>print('text'</code>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "shrugs")
        self.assertEqual(node.to_html(), "<i>shrugs</i>")

    def test_leaf_to_html_value_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode("b", None)

    def test_leaf_to_html_tag_none(self):
        node = LeafNode("", "text")
        self.assertEqual(node.to_html(), "text")

if __name__ == "__main__":
    unittest.main(verbosity=2)



##################################################################################
# parentNode tests