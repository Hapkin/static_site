from src.leafnode import LeafNode, ParentNode
from src.handeler import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images,extract_markdown_links,split_nodes_image, split_nodes_link, text_to_textnodes
from src.textnode import TextNode, TextType
import sys

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
        testing_text_to_textnodes()     

    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
  #      import traceback
 #       traceback.print_exc()

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
          TextNode("**start** bold text", TextType.TEXT),
          TextNode("why so serious **END**", TextType.TEXT),
          TextNode("how about **the middle** of the sentence", TextType.TEXT)
          ]
    test=[
            TextNode("_start_ bold _text_",TextType.TEXT),
            TextNode("why _so_ _serious_ **END**",TextType.TEXT),
        ]
    #result=split_nodes_delimiter(test,"_", TextType.ITALIC)
    #print(result)
     
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