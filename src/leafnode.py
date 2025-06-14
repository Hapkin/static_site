from src.htmlnode import HTMLNode


#We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. 
# It's a node with no children. In this next example,
#True <p>This is a paragraph.</p>
#False! <p>This is a paragraph.<b>This is bold text.</b>This is the last sentence.</p> #<b> is the leaf

class LeafNode(HTMLNode):
    def __init__(self,tag,value, props=None):
        if (value is not None):
            super().__init__(tag, value, props=props)
        else:
            raise ValueError("LeafNode must have a value.")
        
        

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props)

    def to_html(self):
        #print("hello from LeafNode.ToHTML()")
        if self.value == None:
            #print("DEBUG: node missing value:", self)
            raise ValueError("'value' property must contain a value.")
        if self.tag is None or self.tag == "":
            return self.value
        else:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
        


#We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. 
# It's a node with no children. In this next example,
#True <p>This is a paragraph.</p>
#False! <p>This is a paragraph.<b>This is bold text.</b>This is the last sentence.</p> #<b> is the leaf

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag, children=children, props=props)
        
        
        

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and 
                self.children == other.children and 
                self.props == other.props)



    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag prop.")
        if self.children is None:
            raise ValueError("missing children prop.")
        #if(len(self.children)==0 ): => is not the same! Both approaches will trigger if self.children is an empty list. However, only if not self.children: will also catch other falsy values, such as None, '', or False. In your context, since you want to specifically check for empty children, either works fine if you're sure self.children is a list.
        if not self.children:
            raise ValueError("missing children prop.")
        if (type(self.children)!=list):
            raise ValueError("children prop is not a list.")


        props_str = self.props_to_html() if hasattr(self, "props_to_html") else ""
        children_html = "".join(child.to_html() for child in self.children)
        result2=f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
        return result2