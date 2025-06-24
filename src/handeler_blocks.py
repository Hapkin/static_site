from enum import Enum
import re
from dataclasses import dataclass

from src.htmlnode import HTMLNode
from src.leafnode import LeafNode,ParentNode
from src.handeler_text import text_to_textnodes, text_node_to_html_node
from src.textnode import TextNode, TextType

class BlockType(Enum):     
    PARAGRAPH="p"
    HEADING="#"
    CODE="```"
    QUOTE=">"
    UNORDERED_LIST="-"
    ORDERED_LIST="."

@dataclass
class Block():
    text:str #unless its an ordered list!
    block_type: BlockType
    children=[]

    def __repr__(self):
        printstr=""
        if(self.text is not None):
            printstr+=(f"{self.text}\n")
        if(self.block_type is not None):
            printstr+=(f"{self.block_type}\n")
        if(self.children is not None):
            printstr+=(f"{self.children}\n")
        return printstr
    

    #def __init__():
    #    if(block_type is not None):
    #        delimiter=BlockType.value


## opdelen in grote blokken
def markdown_to_blocks(markdown):
    new_blocks=[]
    if(type(markdown)!=str) or (markdown is None) or not (markdown):
        raise ValueError(f"markdown is not a string:{markdown}")
    #regex in case there are hidden spaces between \n\n
    #splitted_markdown=markdown.split("\n\n")
    pattern=r"\n[\s]*\n+"
    splitted_markdown=re.split(pattern,markdown)


    #print(f"{splitted_markdown!r}")
    

    #################
    #2 line solution
    #stripped_items = map(str.strip, splitted_markdown)
    #new_blocks = list(filter(None, stripped_items))
    #1 line solution
    #new_blocks = [item.strip() for item in splitted_markdown if item.strip()]
    ##### for is good
    for item in splitted_markdown:
        item=item.strip()
        if(item is None)or (item==''):
            continue
        #print(f"item: {item!r}")        
        new_blocks.append(item)

    
    #print(f"{new_blocks!r}")
    if not (new_blocks):
        raise NotImplementedError("No blocks where found!")
    return new_blocks
    

def block_to_block_type(block_text):

    if (type(block_text)!=str) or (block_text is None) or (len(block_text)==0):
        raise ValueError(f"block should be text: {block_text}")
    
    if(block_text.startswith("#")):
        pattern=r"^[#]{1,6}\s"
        if (re.match(pattern,block_text)):
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
    elif(block_text.startswith("```"))and(block_text[-3:]==("```"))and(len(block_text)!=3):
        return BlockType.CODE
    elif(block_text.startswith(">")):
        l_lines_in_blocktext=block_text.split("\n")
        check_lines = [word for word in l_lines_in_blocktext if word.startswith(">")]
        if(len(l_lines_in_blocktext)==len(check_lines)):
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH
    elif(block_text.startswith("- ")):
        l_lines_in_blocktext=block_text.split("\n")
        check_lines = [word for word in l_lines_in_blocktext if word.startswith("- ")]
        if(len(l_lines_in_blocktext)==len(check_lines)):
            return BlockType.UNORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    elif(block_text.startswith("1. ")):
        l_lines_in_blocktext=block_text.split("\n")
        line_counter=0
        check_lines=[]
        for line in l_lines_in_blocktext:
            line_counter+=1
            if(line.startswith(f"{line_counter}. ")):
                check_lines.append(line)
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH
