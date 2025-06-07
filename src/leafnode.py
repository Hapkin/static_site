from .htmlnode import HTMLNode


#We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. 
# It's a node with no children. In this next example,
#True <p>This is a paragraph.</p>
#False! <p>This is a paragraph.<b>This is bold text.</b>This is the last sentence.</p> #<b> is the leaf

class LeafNode(HTMLNode):
    def __init__(self,tag,value, props=None):
        if (value is not None):
            super().__init__(tag, value, props)
        else:
            raise ValueError("LeafNode must have a value.")
        
        

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props)

    def to_html(self):
        print("hello from LeafNode.ToHTML()")
        if self.value == None:
            print("DEBUG: node missing value:", self)
            raise ValueError("'value' property must contain a value.")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"