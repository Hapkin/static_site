import unittest
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_prop_types(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com/")
        self.assertEqual(type(node.text), str)
        self.assertEqual(type(node.text_type), TextType)
        self.assertEqual(type(node.url), str)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This a italic node", TextType.ITALIC) #type is different
        self.assertNotEqual(node, node2)
    def test_not_eq_url(self):
        node = TextNode("This is a image node", TextType.IMAGE,"https://www.google.com/")
        node2 = TextNode("This is a image node", TextType.IMAGE,"https://www.google.com") #url is different
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()