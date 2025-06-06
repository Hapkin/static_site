from htmlnode import HTMLNode


#We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. 
# It's a node with no children. In this next example,
#True <p>This is a paragraph.</p>
#False! <p>This is a paragraph.<b>This is bold text.</b>This is the last sentence.</p> #<b> is the leaf

class LeafNode(HTMLNode):
    def __init__(self,tag,value, prop=None):
        if (value is not None):
            super().__init__(tag, value, prop)
        else:
            raise ValueError
        
        

    def __eq__(self, other):
        pass

    def to_html():
        pass