from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

from handeler import text_node_to_html_node

def main():
    my_textnode= TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(my_textnode)
    text_node_to_html_node(my_textnode)








main()