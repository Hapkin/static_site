import re
from src.textnode import TextNode, TextType, ReMatches
from src.leafnode import LeafNode
#import sys
#sys.setrecursionlimit(1000)
#######
'''
def text_node_to_html_node(text_node):
def split_nodes_delimiter(old_nodes, delimiter, texttype):
def extract_markdown_links(text):
def extract_markdown_images(text):
def split_nodes_image(old_nodes):
def split_nodes_link(old_nodes):
def text_to_textnodes(text):
'''
#######


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
        

def split_nodes_bolditalic(old_nodes):
    list_of_nodes=[]
    print(len(old_nodes))
    for node in old_nodes:
        breakpoint()
        if(node.text_type!=TextType.TEXT):
            list_of_nodes.append(node)
            continue

        text=node.text
        pattern_bold=r"\*\*(.*?)\*\*"
        re_bold=re.finditer(pattern_bold,text)
        #lijst maken van de resultaten regex; obj ReMatches(x,y,group1) => group1 is het resultaat zonder**/_
        list_bold = [ReMatches(result.span(), result.group(1)) for result in re_bold]
        
        pattern_italic=r"\_(.*?)\_"
        re_italic=re.finditer(pattern_italic,text)
        list_italic = [ ReMatches(result.span(), result.group(1)) for result in re_italic]
        
        
        #b en i teller dienen om op de juiste match te blijven zitten
        
        b_teller=0
        b_max=len(list_bold)-1

        i_teller=0
        i_max=len(list_italic)-1
        #t teller is waar in de string hij zich bevindt
        t_teller=0
        b_x=0
        b_y=0
        i_x=0
        i_y=0
        while (t_teller<(len(text)-1)):
            laagste_x=t_teller
            
            ##example: list_bold[b_teller][span/group][xy0][group1]
            if(list_bold): 
                b_x=list_bold[b_teller].x
                b_y=list_bold[b_teller].y
            else:
                b_x=float("inf")
                b_y=float("inf")
            #print(f"$ {b_x}, {b_y}") #info
            if(list_italic): 
                i_x=list_italic[i_teller].x
                i_y=list_italic[i_teller].y
            else:
                i_x=float("inf")
                i_y=float("inf")
            #print(f"$ {i_x}, {i_y}") #info
            #print(list_italic[i_teller])

            #print(f"first: laagste_x={laagste_x}=?{t_teller} b_x: {b_x} || i_x: {i_x}")
            #print(f"TEXT: if(laagste_x<b_x)and(laagste_x<i_x): {(laagste_x<b_x)}and{(laagste_x<i_x)}")
            #print(f"BOLD: elif(b_x<i_x): ({b_x}<{i_x}): b_teller={b_teller}")
            #print(f"ITAL: elif(i_x<b_x): ({i_x}<{b_x}): i_teller={i_teller}")
            
            if(laagste_x<b_x)and(laagste_x<i_x):
                
                #laagste_x is de laagste dus is het een textfield
                if(b_x<i_x):
                    laagste_x=b_x
                else:
                    laagste_x=i_x
                if(laagste_x==float("inf")):
                    laagste_x= len(text)

                new_node= TextNode(text[t_teller:laagste_x],TextType.TEXT)
                list_of_nodes.append(new_node)
                #teller gelijk zetten naar laagste x (kan bold of italic zijn)
                t_teller=laagste_x
            elif(b_x<i_x):
                laagste_x=b_x
                #laagste_x is een bold item
                while(b_y>i_y):
                    #er zit een italic item in deze BOLD!!
                    new_node= TextNode(list_bold[b_teller].group,TextType.BOLD, IB="_") #IB toegevoegd om later parentnode te maken
                    if(i_teller<len(list_italic)):
                        i_teller+=1 #? wat als er 2 italic items inzitten... while!
                        i_x=list_italic[i_teller].x
                        i_y=list_italic[i_teller].y
                    
                    else:
                        list_of_nodes.append(new_node)
                        if(b_teller<b_max):
                            b_teller+=1
                        else:
                            list_bold[b_teller].x=float("inf")
                            list_bold[b_teller].y=float("inf")
                        break
                #als b_y kleiner is dan is het volgende italic element buiten deze bold
                new_node= TextNode(list_bold[b_teller].group,TextType.BOLD)
                list_of_nodes.append(new_node)
                if(b_teller<b_max):
                    b_teller+=1
                else:
                    list_bold[b_teller].x=float("inf")
                    list_bold[b_teller].y=float("inf")
                #string verder zetten naar einde van huidige bold
                t_teller=b_y
            elif(i_x<b_x):
                laagste_x=i_x
                #laagste_x is een bold item
                while(i_y>b_y):
                    #er zit een italic item in deze BOLD!!
                    new_node= TextNode(list_italic[i_teller].group,TextType.ITALIC, IB="**") 
                    

                    if(b_teller<b_max):
                        b_teller+=1 #? wat als er 2 italic items inzitten... while!
                        b_x=list_bold[b_teller].x
                        b_y=list_bold[b_teller].y
                    else:
                        list_of_nodes.append(new_node)
                        if(i_teller<i_max):
                            i_teller+=1
                        else:
                            list_italic[i_teller].x=float("inf")
                            list_italic[i_teller].y=float("inf")
                        break
                #als b_y kleiner is dan is het volgende italic element buiten deze bold
                new_node= TextNode(list_italic[i_teller].group,TextType.ITALIC)
                list_of_nodes.append(new_node)
                if(i_teller<i_max):
                    i_teller+=1
                else:
                    list_italic[i_teller].x=float("inf")
                    list_italic[i_teller].y=float("inf")
                #string verder zetten naar einde van huidige bold
                t_teller=i_y
            else:
                 raise ValueError("hier zou hij niet mogen komen...")
    return list_of_nodes


#moeten eerst TextNodes worden daarma .text_node_to_html_node()
#old nodes zijn textnodes!! []
def split_nodes_delimiter(old_nodes, delimiter, texttype):
    list_new_nodes=[]
    len_delimiter=len(delimiter)
    
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("oldnodes: this is not a TextNode")
        if (node.text_type != TextType.TEXT):
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
            
    breakpoint()
    return list_new_nodes

#[to boot dev](https://www.boot.dev)
def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

#![image](https://i.imgur.com/zjjcJKZ.png)
def extract_markdown_images(text):
    pattern = r"!\[([^\]]*)\]\(([^\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

r'''  WITH MORE DEBUGGING!!
def extract_markdown_images(text):
    print("Function called with text:", text[:50], "...")  # Debug line
    try:
        import re
        print("re module imported successfully")  # Debug line
        pattern = r"!\[([^\]]*)\]\(([^\)]*)\)"
        print("Pattern created:", pattern)  # Debug line
        matches = re.findall(pattern, text)
        print("Matches found:", matches)  # Debug line
        return matches
    except Exception as e:
        print("Error occurred:", e)
        raise
'''

def split_nodes_image(old_nodes):
    new_nodes = []
    if isinstance(old_nodes, list):
        if not old_nodes:
            raise ValueError(f"split_nodes_image: no items in {old_nodes}...")
    else:
        raise ValueError(f"oldnodes: this is not a list of nodes {old_nodes}...")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise ValueError("oldnodes: this is not a TextNode")
        #convert text ![]() => ImageNode
        
        images=extract_markdown_images(node.text)
        #if there is no result there are no valid image tags in this node!
        if not (images):
            if node.text.strip():  # Only append if text is not empty/whitespace
                new_nodes.append(node)
            continue

        left_over=node.text.split("![",1)
        #check if text starts with an image
        if(len(left_over[0])==0):
            new_nodes.append(TextNode(images[0][0],TextType.IMAGE,images[0][1]))
            
            removed_image=left_over[1].split(")",1)
            if(len(removed_image[1])>2):
                next_string=f"{removed_image[1]}"
            else:
                continue
        else:
            if left_over[0].strip():  # Only append if text is not empty/whitespace
                new_nodes.append(TextNode(left_over[0],TextType.TEXT))
            if(len(left_over)==2):
                next_string=f"![{left_over[1]}"
        new_nodes.extend(split_nodes_image([TextNode(next_string,TextType.TEXT)]))
        
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    if isinstance(old_nodes, list):
        if not old_nodes:
            raise ValueError(f"split_nodes_link: no items in {old_nodes}...")
    else:
        raise ValueError(f"oldnodes: this is not a list of nodes {old_nodes}...")
    for node in old_nodes:
        #print(f"Processing node: {node.text[:50]}...")
        if not isinstance(node, TextNode):
            raise ValueError("oldnodes: this is not a TextNode")
        #convert text []() => TextType.LINK
        
        images=extract_markdown_links(node.text)
        #if there is no result there are no valid image tags in this node!
        if not (images):
            if node.text.strip():  # Only append if text is not empty/whitespace
                new_nodes.append(node)
            #print(f"images left? :: {images}")
            continue

        left_over=node.text.split("[",1)
        #check if text starts with an image
        if(len(left_over[0])==0):
            new_nodes.append(TextNode(images[0][0],TextType.LINK,images[0][1]))
            removed_image=left_over[1].split(")",1)
            if(len(removed_image[1])>2):
                next_string=f"{removed_image[1]}"
            else:
                continue
        else:
            if node.text.strip():  # Only append if text is not empty/whitespace
                new_nodes.append(TextNode(left_over[0],TextType.TEXT))
            if(len(left_over)==2):
                next_string=f"[{left_over[1]}"
        new_nodes.extend(split_nodes_link([TextNode(next_string,TextType.TEXT)]))
        
    return new_nodes




def text_to_textnodes(text):
    #This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
    if not type(text)==str :
        raise ValueError(f"(text) should be a string: {text}")
    if(len(text.strip())==0):
       raise ValueError(f"(text) shouldn't be empty: {text}")

    new_nodes_list = []
    old_nodes = [TextNode(text, TextType.TEXT)]
    #this will split all the codes into nodes, and if ** or _ is present keep them intact within the ``` code-tag
    new_nodes_list = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
    #order matters you can have _ within ** or within ``, but not the other way arround
    # if I try to fix this within split_nodes_delimiter() I will brake the code ``` piece that should keep ** and _ intact
    # unless I make an optional argument? list of delimiters and try to do both ** and _ simultanios... let's see 
    #not working without a lot of refactoring; other option now it skips all not TextType.TEXT as processed
    #what if we add BOLD and ITALIC as not processed type so it will still look within 
    # not working because then it will close the tag in another node... break
    # would need to make a seperate function like link and image... but that was not the idea
    #new_nodes_list = split_nodes_delimiter(new_nodes_list, "**", TextType.BOLD)
    #new_nodes_list = split_nodes_delimiter(new_nodes_list, "_", TextType.ITALIC)
    new_nodes_list= split_nodes_bolditalic(new_nodes_list)
    new_nodes_list = split_nodes_link(new_nodes_list)
    new_nodes_list = split_nodes_image(new_nodes_list)
    return new_nodes_list

