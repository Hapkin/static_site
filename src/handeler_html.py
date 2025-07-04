import re
from src.leafnode import ParentNode, LeafNode
from src.handeler_text import text_to_textnodes, text_node_to_html_node, TextType, TextNode
from src.handeler_blocks import  Block, markdown_to_blocks, block_to_block_type, BlockType

#TextNode-> HTMLNode  => <blockquote>; <UL>; <OL> <pre><code>
def markdown_to_html_node(markdown):
    if(markdown is not None) or not isinstance(markdown, str) or (markdown==""):
        ValueError(f"not right format: {markdown}")
    my_parent_div=ParentNode("div",children=None)
    
    my_block_texts=markdown_to_blocks(markdown)
    my_block_types=[block_to_block_type(block) for block in my_block_texts]
    my_blocks=[]
    
    for i in range(0,(len(my_block_texts))):
        new_block= Block(my_block_texts[i],my_block_types[i])
        my_blocks.append(new_block)
    html_nodes_created_from_my_blocks=[]
    for block in my_blocks:
        if block.block_type != BlockType.CODE:
            block.children=text_to_textnodes(block.text)
        html_nodes_created_from_my_blocks.append(block_to_html(block))
    
        
    my_parent_div.children=html_nodes_created_from_my_blocks
    #print(my_parent_div.to_html())
    return my_parent_div
    

#
def textnodes_to_htmlnodes(list_textnodes):
    if(list_textnodes is None) or not isinstance(list_textnodes, list) or not (list_textnodes):
        ValueError(f"not right format: {list_textnodes}")
    htmlnodes=[]
    for textnode in list_textnodes:
        html_node = text_node_to_html_node(textnode)
        htmlnodes.append(html_node)
    return htmlnodes
    
def block_to_html(block):
    if(not isinstance(block, Block)):
        raise ValueError(" block_to_html_node(block) it's not a block")
    ## still need a BlockType.PARAGRAPH converter....
    if(block.block_type==BlockType.HEADING):
        #counts number of # ending with a space but the ()-group will not count the space char
        pattern=r"^([#]{1,6})[\s]"   
        count=len(re.search(pattern,block.text).group(1))
        #removes count chars
        new_text=block.text[count:].strip()
        #nakijken of er andere formats in de text zitten!!!
        
        new_textnodes=text_to_textnodes(new_text)
        leaf_children=textnodes_to_htmlnodes(new_textnodes)
        return ParentNode(f"h{count}",leaf_children)

        

    elif block.block_type == BlockType.CODE:
        new_text=block.text.strip()
        new_text = new_text[3:-3].lstrip()  # Strip the ``` and extra \n\s
        code_node = LeafNode("code", new_text)
        return ParentNode("pre", [code_node])

    elif(block.block_type==BlockType.QUOTE):
        #mistake you need to check if there are other types inside the quote text like bold, italic
        #lines = [LeafNode("q", word[1:] ) for word in l_lines_in_blocktext if word.startswith(">")]
        new_leafs=[]
        l_lines_in_blocktext=block.text.split("\n")
        for line in l_lines_in_blocktext:
            stripped_line = line[1:]
            stripped_line =stripped_line.strip()
            # if a single ">" is found skip it 
            if(len(stripped_line)==0):
                continue    
            new_textnodes=text_to_textnodes(stripped_line)
            for item in new_textnodes:
                new_leafs.append(item)
            new_leafs.append(TextNode("\n",TextType.TEXT))
        
        # Remove the trailing newline
        new_leafs.pop()
        result=textnodes_to_htmlnodes(new_leafs)
        result= ParentNode("blockquote", result)
        return result
    

    elif(block.block_type==BlockType.UNORDERED_LIST):
        list_li=[]
        
        l_lines_in_blocktext=block.text.split("\n")
        #print(l_lines_in_blocktext)
        for line in l_lines_in_blocktext:
            new_leafs=[]
            stripped_line=line.strip()[2:]
            new_textnodes=text_to_textnodes(stripped_line)

            result=textnodes_to_htmlnodes(new_textnodes)
            list_li.append(ParentNode("li",result)) 
        result= ParentNode("ul", list_li)
        return result
        
    elif(block.block_type==BlockType.ORDERED_LIST):
        list_li=[]
        counter=0
        l_lines_in_blocktext=block.text.split("\n")
        #print(l_lines_in_blocktext)
        for line in l_lines_in_blocktext:
            new_leafs=[]
            #counter 1-9 remove 3 char 10-19 remove 4
            counter+=1
            counter_div10=int((counter/10)+1)
            stripped_line=line.strip()[(2+counter_div10):]
            new_textnodes=text_to_textnodes(stripped_line)

            result=textnodes_to_htmlnodes(new_textnodes)
            list_li.append(ParentNode("li",result)) 
        result= ParentNode("ol", list_li)
        return result
    
    else:
        if(block.block_type!=BlockType.PARAGRAPH):
            raise Exception(f"This should never happen! BlockType!=PARAGRAPH {block.block_type} is last of possibilitys!")
        leaf_children=[]

        #print(l_lines_in_blocktext)
        stripped_line=block.text.strip().replace('\n', ' ')
        new_textnodes=text_to_textnodes(stripped_line)
        leaf_children=textnodes_to_htmlnodes(new_textnodes)
        return ParentNode("p", leaf_children)
    

# simple check if html_template is a full html document (used in multiple locations)
def check_html(html_template):
    if(html_template!=str): 
        return False
    html_template=html_template.strip()
    if ((html_template.startswith("<!doctype html>"))) or (html_template.startswith("<html>")) and (html_template.endswith("</html>")):
        return True
    else:
        return False