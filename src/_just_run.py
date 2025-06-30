import sys
import re
from src.leafnode import LeafNode, ParentNode
from src.handeler_text import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images,extract_markdown_links,split_nodes_image, split_nodes_link, text_to_textnodes
from src.handeler_blocks import markdown_to_blocks
from src.handeler_html import markdown_to_html_node, textnodes_to_htmlnodes
from src.textnode import TextNode, TextType
from src.handeler_blocks import BlockType
from src.handler_IO import delete_folder, copy_folder_to_folder

def main():
    try:
        pass
        #print("hello from main")
        #testing_leaf()
        #testing_parent()
        #test_TEXTNode()
        #print("fool")
        #test_split_nodes_delimiter()
        # Test with the absolute simplest case first
        #print(testing_split_nodes_image())
        #testing_text_to_textnodes()     
        #result=testingmarkdown_to_blocks()
        #test_quoteblock()
        #result=test_p()
        #breakpoint()
        
        path_to_del="./public"
        path_to_from="./static"
        path_to="./public"
        #delete_folder(path_to_del)
        copy_folder_to_folder(path_to_from,path_to)
#        quit()

    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
  #      import traceback
 #       traceback.print_exc()



r'''
        text="""
# My Grand Adventure Log

This is a **simple paragraph** to start things off. It also has some _italic_ text and a piece of `code_snippet()`.

## Chapter 1: The Mysterious Forest

### A Deep, Dark Place

> "Beware the Whispering Willows," whispered the old hermit.
> "Their roots run deep, and their secrets deeper still."

### Strange Discoveries

- Found a shimmering **blue** mushroom.
- Heard a peculiar bird song.
- Noticed ancient symbols carved into trees:

- First symbol: `circle`
- Second symbol: `triangle`
- Third symbol: `square`

### The Path Less Traveled

1.  Follow the mossy stones.
2.  Cross the bubbling brook.
3.  Ascend the **Screaming** Peak.

1.  Pack warm clothes.
2.  Bring extra ropes.

#### A Glimmer of Hope

We saw a faint light in the distance. It looked like a small `campfire`.

> "Could it be a friend?" I wondered aloud.
```function lightFire() {
console.log("Fire started!");
}
lightFire();```

###### End of Log Entry

This is another paragraph just to ensure multi-paragraph handling is correct. It's a very *long* paragraph that wraps around a bit to test that too. What a journey!
"""
        print(markdown_to_html_node(text).to_html())
'''
        
             
        


def test_p():
    block_text="""This is another paragraph with _this is in italic_ fsdfs
    text and ```this is code``` here"""
    leaf_children=[]

    #print(l_lines_in_blocktext)
    stripped_line=block_text.strip()
    new_textnodes=text_to_textnodes(stripped_line)
    leaf_children=textnodes_to_htmlnodes(new_textnodes)
    return ParentNode("p", leaf_children)
    

def test_ul():
    text="""> 1This is another paragraph with _this is in italic_ fsdfs
    > 2text and ```this is code``` here"""
    list_li=[]
    
    l_lines_in_blocktext=text.split("\n")
    #print(l_lines_in_blocktext)
    for line in l_lines_in_blocktext:
        new_leafs=[]
        stripped_line=line.strip()[2:]
        new_textnodes=text_to_textnodes(stripped_line)

        result=textnodes_to_htmlnodes(new_textnodes)
        list_li.append(ParentNode("li",result)) 
    result= ParentNode("ul", list_li)
    
    print(result.to_html())    


def test_quoteblock():
        text=""">This is another paragraph with _this is in italic_ fsdfs
        >text and ```this is code``` here"""
        #mistake you need to check if there are other types inside the quote text like bold, italic
        #lines = [LeafNode("q", word[1:] ) for word in l_lines_in_blocktext if word.startswith(">")]
        new_leafs=[]
        l_lines_in_blocktext=text.split("\n")
        for line in l_lines_in_blocktext:
            stripped_line =line.strip()
            stripped_line = stripped_line[1:]
            new_textnodes=text_to_textnodes(stripped_line)
            for item in new_textnodes:
                new_leafs.append(item)
            new_leafs.append(TextNode("\n",TextType.TEXT))
        
        # Remove the trailing newline
        new_leafs.pop()
        result=textnodes_to_htmlnodes(new_leafs)
        result= ParentNode("blockquote", result)
        print(result.to_html())


def testingmarkdown_to_blocks():
     text="""# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
  
    

- This is the first list item in a list block
- This is a list item
- This is another list item"""
     text="""
This is **bolded** paragraph
     
    

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
  
    
  
    

- This is a list
- with items
"""
     result=markdown_to_blocks(text)
     #print(repr(result))
     return result

def testing_text_to_textnodes():
    pass
    #text="This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text = "**bold**_italic_"
    print(text_to_textnodes(text))


def testing_split_nodes_image():
    simple_text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
    print("=== SIMPLE TEST ===")
    #print(extract_markdown_links(simple_text))
    result=split_nodes_link([simple_text])
    print(f"\n=========\n {result}") 


    print("\n=== COMPLEX TEST ===") 
    # Then test with your complex text
    node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) " \
        "![rick roll](https://i.imgur.com/aKaOqIh.gif)" \
        " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" \
        " and ![abi (https://i.jpeg)", \
        TextType.TEXT)
    #node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev)", TextType.TEXT)        
    #node2 = TextNode("![to boot dev](https://www.boot.dev)![to boot dev](https://www.boot.dev)![to boot dev](https://www.boot.dev)", TextType.TEXT)        
    #node3 = TextNode("![to boot dev](https://www.boot.dev)", TextType.TEXT)        
    #node4 = TextNode("![to boot dev](https://www.boot.dev)This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)        
    #node5 = TextNode("", TextType.TEXT)        
    #node6 = TextNode("This is text ![to boot dev](https://www.boot.dev) with a link ", TextType.TEXT)        
    #node7 = TextNode("![to boot dev](https://www.boot.dev) This is text with a link ", TextType.TEXT)        
    
    #print(extract_markdown_images(node.text))
    #print(extract_markdown_images("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"))
    #print(extract_markdown_links(text))
    #sys.exit()
    #result=split_nodes_image([node,node2,node3,node4,node5,node6,node7])
    result=split_nodes_image([node])
    return (f"\n=========\n {result}")

def testing_leaf():
        # Test your LeafNode here
        node = LeafNode("p", "Hello, world!")
        print(node.to_html())
        
        # Test with attributes
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node2.to_html())
        
        # Test with no tag
        node3 = LeafNode(None, "Just plain text")
        print(node3.to_html())

def testing_parent():    
        #node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        node = ParentNode("p", children=[LeafNode("b", "Bold text")], props={"style":"color:green"})
        node2 = ParentNode("h1",children=[node], props={"href":"https://www.google.be","target":"_blanc"})
        node3 = ParentNode("a",children=[node2], props={"href":"https://www.google.be","target":"_new"})
        #print(f"1->: {node}")
        #<a><h1><p><b>Bold text</b></p></h1></a>
        print(node.to_html())
        print("=========")
        print(node2.to_html())
        print("=========")
        print(node3.to_html())

def test_TEXTNode():
    #node = TextNode("This is a text node", TextType.TEXT)
    node = TextNode("Go bears!", TextType.LINK, "http://whatever.com")
    html_node = text_node_to_html_node(node)
    print(html_node)

def test_split_nodes_delimiter():
     #text=[ TextNode( '**This** is text with a **bolded phrase** in the middle', TextType.TEXT)] 
          
     
    text=[
          TextNode("This is a **simple paragraph** to start things off. It also has some _italic_ text and a piece of ```codesnippet()```.", TextType.TEXT),
          ]
    test=[
            TextNode("_start_ bold _text_",TextType.TEXT),
            TextNode("why _so_ _serious_ **END**",TextType.TEXT),
        ]
    result=split_nodes_delimiter(text,"_", TextType.ITALIC)
    print(result)
    return
     
    delimiter = "**"
    text_type= TextType.CODE
    result= split_nodes_delimiter(text, delimiter, TextType.BOLD)
    print(result)
    #for item in result:
    #     print(type(item))
    #     print(f"{item}\n")

#if __name__ == "__main__":
main()
#else:
#     print("failed run")