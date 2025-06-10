from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.handeler import text_node_to_html_node
from src.textnode import TextNode, TextType

def main():
    try:
        pass
        #print("hello from main")
        #testing_leaf()
        #testing_parent()
        test_TEXTNode()
        #print("fool")


    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

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


#if __name__ == "__main__":
main()
#else:
#     print("failed run")