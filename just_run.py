from src.leafnode import LeafNode
from src.parentnode import ParentNode

def main():
    try:
        print("hello from main")
        #testing_leaf()
        testing_parent()


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
        node = ParentNode(
                "p",
                [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
            )
        print(node.to_html())


if __name__ == "__main__":
    main()