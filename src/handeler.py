from src.textnode import TextNode, TextType
from src.leafnode import LeafNode



def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError(f"{text_node.text_type} is not a valid TextType.")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", value=text_node.text)
        case TextType.CODE:
            return LeafNode("code", value=text_node.text)
        case TextType.LINK:
            return LeafNode("a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError(f"Error:{text_node.text_type} is not a valid TextType?.?")