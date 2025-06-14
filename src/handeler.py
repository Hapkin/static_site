import re
from src.textnode import TextNode, TextType
from src.leafnode import LeafNode
import sys
sys.setrecursionlimit(25)



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
        

'''
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),

    class TextType(Enum):    
    TEXT = "text"       #"Normal text"
    BOLD = "bold"       #"**Bold text**"
    ITALIC = "italic"   #"_Italic text_"
    CODE = "code"       #"`Code text`"
    LINK = "link"       #"[anchor text](url)"
    IMAGE = "image"     #"![alt text](url)"
]'''


#moeten eerst TextNodes worden daarma .text_node_to_html_node()
#old nodes zijn textnodes!!
def split_nodes_delimiter(old_nodes, delimiter, texttype):
    list_new_nodes=[]
    len_delimiter=len(delimiter)
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("oldnodes: this is not a TextNode")
        if node.text_type != TextType.TEXT:
            list_new_nodes.append(node)
            continue  #skip all code below and continue for loop (old_nodes)
        text=node.text
        int_delimiter=text.find(delimiter)
        #print(f"delimiter: {delimiter} - {len_delimiter}")
        #print(f"found {delimiter} - {int_delimiter} ==> {text[len_delimiter:]}")
        #if the delimiter is not found just add the entire node 
        if(int_delimiter==-1):
            list_new_nodes.append(node)
            continue
        #firstchar is delimiter
        elif(int_delimiter==0):
            #remove delimiter
            my_string=text[len_delimiter:]
            #print(f"my_string:{my_string}")
            #search again to find close tag
            int_delimiter=my_string.find(delimiter)
            #if not found error must be raised there is no end-tag!!
            if(int_delimiter==-1):
                raise ValueError(f"closing tag not found:{delimiter}||{my_string}")
            #remove all behind close tag
            new_code_string=my_string[:int_delimiter]
            #print(f"new_code_string: {new_code_string}")
            #turn into a leaf
            new_text=TextNode(new_code_string, texttype)
            list_new_nodes.append(new_text)
            #continue node
            text=my_string[int_delimiter:]
            text=text[len_delimiter:]
            #print(f"text leftover elif: {text}\n ")
        else:
            my_string=text[0:int_delimiter]
            new_text=TextNode(my_string, TextType.TEXT)
            list_new_nodes.append(new_text)
            text=text[int_delimiter:]
            #print(f"text leftover else: {text}\n ")
        
        if(len(text)!=0):
            new_textnode=TextNode(text, TextType.TEXT)
            list_new_nodes.extend(split_nodes_delimiter([new_textnode],delimiter, texttype))
            
    return list_new_nodes