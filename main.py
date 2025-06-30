from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
from src.handler_IO import copy_folder_to_folder
from src.handeler_text import text_node_to_html_node

def main():
    path_to_from="./static"
    path_to="./public"
    #delete_folder(path_to_del)
    copy_folder_to_folder(path_to_from,path_to)
    
    my_textnode= TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(my_textnode)
    text_node_to_html_node(my_textnode)








main()