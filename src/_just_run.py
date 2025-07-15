import sys
import re
from src.leafnode import LeafNode, ParentNode
from src.handeler_text import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images,extract_markdown_links,split_nodes_image, split_nodes_link, text_to_textnodes
from src.handeler_blocks import markdown_to_blocks
from src.handeler_html import markdown_to_html_node, textnodes_to_htmlnodes
from src.textnode import TextNode, TextType, ReMatches
from src.handeler_blocks import BlockType
from src.handler_IO import delete_folder, copy_folder_to_folder, read_files_in_folder
from src.generate_pages import extract_title,generate_page, generate_all_pages_static


def main():
    try:
        pass
        #test_split_nodes_delimiter()
        text="_H**e**l**l**o_, welcome **to _my_ world**. This, _is a_ test, _for **BOLD** moves_**.** abc"
        pattern_bold=r"\*\*(.*?)\*\*"
        re_bold=re.finditer(pattern_bold,text)
        #lijst maken van de resultaten regex; obj ReMatches(x,y,group1) => group1 is het resultaat zonder**/_
        list_bold = [ReMatches(result.span(), result.group(1)) for result in re_bold]
        
        pattern_italic=r"\_(.*?)\_"
        re_italic=re.finditer(pattern_italic,text)
        list_italic = [ ReMatches(result.span(), result.group(1)) for result in re_italic]
        
        list_of_nodes=[]
        #b en i teller dienen om op de juiste match te blijven zitten
        b_teller=0
        i_teller=0
        #t teller is waar in de string hij zich bevindt
        t_teller=0
        while (t_teller<len(text)):
            laagste_x=t_teller
            
            print(f"first {list_bold[b_teller].x} : {list_bold[b_teller].y}")
            print(t_teller)
            breakpoint()
            ##example: list_bold[b_teller][span/group][xy0][group1]
            b_x=list_bold[b_teller].x
            b_y=list_bold[b_teller].y
            print(f"$ {b_x}, {b_y}") #info
            i_x=list_italic[i_teller].x
            i_y=list_italic[i_teller].y
            print(f"$ {i_x}, {i_y}") #info
            print(list_italic[i_teller])
            if(laagste_x<b_x)and(laagste_x<i_x):
                #laagste_x is de laagste dus is het een textfield
                if(b_x<i_x):
                    laagste_x=b_x
                else:
                    laagste_x=i_x

                new_node= TextNode(text[t_teller:laagste_x],TextType.TEXT)
                list_of_nodes.append(new_node)
                #teller gelijk zetten naar laagste x (kan bold of italic zijn)
                t_teller=laagste_x
            elif(b_x<i_x):
                laagste_x=b_x
                #laagste_x is een bold item
                while(b_y>i_y):
                    #er zit een italic item in deze BOLD!!
                    new_node= TextNode(text[b_x:b_y],TextType.BOLD, IB="_") #IB toegevoegd om later parentnode te maken
                    list_of_nodes.append(new_node)
                    if(b_teller<len(list_bold)):
                        b_teller+=1
                    if(i_teller<len(list_italic)):
                        i_teller+=1 #? wat als er 2 italic items inzitten... while!
                        i_x=list_italic[i_teller].x
                        i_y=list_italic[i_teller].y
                    else:
                        break
                #als b_y kleiner is dan is het volgende italic element buiten deze bold
                new_node= TextNode(text[b_x:b_y],TextType.BOLD)
                list_of_nodes.append(new_node)
                if(b_teller<len(list_bold)):
                    b_teller+=1
                #string verder zetten naar einde van huidige bold
                t_teller=b_y
            elif(i_x<b_x):
                laagste_x=i_x
                #laagste_x is een bold item
                while(i_y>b_y):
                    #er zit een italic item in deze BOLD!!
                    new_node= TextNode(text[i_x:i_y],TextType.ITALIC, IB="**") 
                    list_of_nodes.append(new_node)
                    if(i_teller<len(list_italic)):
                        i_teller+=1
                    if(b_teller<len(list_bold)):
                        b_teller+=1 
                        b_x=list_bold[b_teller].x
                        b_y=list_bold[b_teller].y
                    else:
                        break

                #als i_y kleiner is dan is het volgende italic element buiten deze bold
                new_node= TextNode(text[i_x:i_y],TextType.ITALIC)
                list_of_nodes.append(new_node)
                if(i_teller<len(list_italic)):
                    i_teller+=1
                #string verder zetten naar einde van huidige bold
                t_teller=i_y
            else:
                 raise ValueError("hier zou hij niet mogen komen...")
                     
            

            #
            


            '''
            for i in all_bold:
                #location of the bold 
                i_span=i.span()
                
                #this gives the value without **?**
                #print(i.group(1))
                for j in all_italic:
                    j_span=j.span()

                    print(j.group(1))
                    #first check if i(x,y) i[y]<j[x] dan kan er geen meer in deze i coordinaten liggen
                    if(i_span[1]<j_span[0]):
                        break
                    #als i[x]<j[x] en i[y]>i[y] dan hebben we parent van ITALIC met BOLD erin?
                    if(i_span[0]>j_span[0])and(i_span[1]<j_span[1]):
                        print(f"%% {text[j_span[0]:j_span[1]]}")
                    else:
                        pass
'''
        
        
        
        


        #print("hello from main")
        #testing_leaf()
        #testing_parent()
        #test_TEXTNode()
        #print("fool")
        
        # Test with the absolute simplest case first
        #print(testing_split_nodes_image())
        #testing_text_to_textnodes()     
        #result=testingmarkdown_to_blocks()
        #test_quoteblock()
        #result=test_p()
        #breakpoint()
        #----------
        #path_to_del="./public"
        #delete_folder(path_to_del)
        #copy_folder_to_folder(path_to_from,path_to)
        #md= "# test\n# gddfg dfsdf"
        #text= md.split("\n",1)
        #text_left=text[1]
        #print(extract_title(text[0]))
        #print(text_left)
        #list1=[TextNode('![JRR Tolkien sitting](/images/tolkien.png)', TextType.TEXT)]
        #print(split_nodes_image(list1))
        #generate_page("content/index.md","template.html","public/index.html")
        #read_files_in_folder("content/")
        #generate_all_pages_static("/")
        #        quit()

    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
  #      import traceback
 #       traceback.print_exc()
     
             
        


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
        result= ParentNode("blockquote", result.strip())
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
    text=[ TextNode( 'This is _text with a **bolded phrase** in_ the middle', TextType.TEXT)] 
          
     
    text=[
          TextNode("This is a **simple paragraph _to_ start things** off. It also has some _italic_ text and a piece of.", TextType.TEXT),
          ]
    return 0
     
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