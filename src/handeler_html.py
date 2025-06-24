import re
from src.leafnode import ParentNode, LeafNode
from src.handeler_text import text_to_textnodes, text_node_to_html_node
from src.handeler_blocks import  Block, markdown_to_blocks, block_to_block_type


#####???? .to_html()####
def tag(*args): #just return tag front and end
    if (args is None):
        return(f"<{tag}>",f"</{tag}>")
    else:
        ##TODO 
        print("TAGS NOG INCOMPLETE")
        return(f"<{tag}>",f"</{tag}>")



#TextNode-> HTMLNode  => <blockquote>; <UL>; <OL> <pre><code>
def markdown_to_html_node(markdown):
    if(markdown is not None) or not isinstance(markdown, str) or (markdown==""):
        ValueError(f"not right format: {markdown}")
    my_parent_div=ParentNode("div",children=None)
    
    
    #print(f"1 tags::{my_parent}")
    
    my_block_texts=markdown_to_blocks(markdown)
    my_block_types=[block_to_block_type(block) for block in my_block_texts]
    my_blocks=[]

    for i in range(0,(len(my_block_texts))):
        new_block= Block(my_block_texts[i],my_block_types[i])
        my_blocks.append(new_block)
    print(f"{type(my_blocks)}")
    print(f"&&&&")
    print(f"{my_blocks}")
    print(f"&&&&")
    for block in my_blocks:
        #block.children=text_to_textnodes(block.text)
        print(block)
        ####this!
        block_parentnode=ParentNode(block.text, None)
        block_parentnode.children=block.children
        result=textnodes_to_html(block)

    print("########123")
    print(my_blocks)

    #my_parent_div.children=my_blocks
    #return my_parent_div
    

#
def textnodes_to_html(list_textnodes):
    if(list_textnodes is None) or not isinstance(list_textnodes, list) or not (list_textnodes):
        ValueError(f"not right format: {list_textnodes}")
    htmlnodes=[]
    for textnode in list_textnodes:
        html_node = text_node_to_html_node(textnode)
        htmlnodes.append(html_node)
        if(textnode.children is not None):
            htmlnodes.extend(textnode.children)
    print("%%%%%%%%%%%%%%%%%%%%%%%")
    print(htmlnodes)


    
    return htmlnodes
    


r'''
    match block_text[0]:
        case "#":
            #count number of # in front
            pattern="^[#]+"
            number_of_h=len(re.match(pattern,block_text).group(0))
            if(number_of_h>6):
                raise ValueError("max 6 # for a <h>-tag")
            new_block= Block(block_text[number_of_h:], BlockType.HEADING, number_of_h)
            return new_block
        case "```":
            new_block= Block(block_text[3:], BlockType.CODE)
            return new_block
        case ">":
            new_block= Block(block_text[1:], BlockType.QUOTE)
            return new_block
        case "- ":
            pattern="[-][\s]"
            ordered_listitems=list(re.split(pattern,block_text))
            new_block= Block(ordered_listitems, BlockType.UNORDERED_LIST,len(ordered_listitems))
            return new_block
        case ". ":
            pattern="[.][\s]"
            ordered_listitems=list(re.split(pattern,block_text))
            new_block= Block(ordered_listitems, BlockType.ORDERED_LIST, len(ordered_listitems))
            return new_block
        case _:
            return new_block
   
'''