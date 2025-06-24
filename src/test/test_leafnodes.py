import unittest
import inspect
from src.leafnode import LeafNode
''' ##INFO## 7 tests
    def __init__(self,tag,value, props=None):
        if (value is not None):
            super().__init__(tag, value, props)
        else:
            raise ValueError("LeafNode must have a value.")
'''
class TestLeafNode(unittest.TestCase):
    #print("DEBUG: TestLeafNode class loaded")
    def test_properties_types_leaf(self):
        node1 = LeafNode("a","my_url", props={"href":"https://www.google.be","target":"_blanc"})
       
        
        self.assertEqual(type(node1.tag), str)
        self.assertEqual(type(node1.value), str)
        self.assertEqual(type(node1.props), dict)

class TestLeafNode2(unittest.TestCase):
    #print("DEBUG: TestLeafNode2 class loaded")
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "text")
        result=node.to_html()
        self.assertEqual(result, "<p>text</p>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "print('text'")
        result=node.to_html()
        self.assertEqual(result, "<code>print('text'</code>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "shrugs")
        result=node.to_html()
        self.assertEqual(result, "<i>shrugs</i>")

    def test_leaf_to_html_value_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode("b", None)

    def test_leaf_to_html_tag_none(self):
        node = LeafNode("", "text")
        result=node.to_html()
        self.assertEqual(result, "text")


class TestleafNodeStrRepr(unittest.TestCase):
    #print("DEBUG: TestHtmlNodeStrRepr1 class loaded")
    def test_leafnode_str_repr_safe(self):
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
    

    

if __name__ == "__main__":
    unittest.main(verbosity=2)