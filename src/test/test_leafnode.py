import unittest
from ..leafnode import LeafNode
''' ##INFO##


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



if __name__ == "__main__":
    unittest.main(verbosity=2)