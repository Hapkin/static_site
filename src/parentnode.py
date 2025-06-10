from src.htmlnode import HTMLNode
from src.leafnode import LeafNode


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
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
    






'''
### works but it can be done a lot easier

    def to_html(self):
        if (self.children is None) :
            raise ValueError("missing children prop.")
        if(self.tag is None):
            raise ValueError("missing tag prop.")
        list_of_childs=rec_props_to_html(self)

        result=f"".join(list_of_childs)
        return result






## recursion_to_html
def rec_props_to_html(my_node):
    file_list = []
    if(my_node.value is None):
        my_leaf=LeafNode(my_node.tag, "", my_node.props)
    else:
        my_leaf=LeafNode(my_node.tag, my_node.value, my_node.props)
    current_leaf=my_leaf.to_html()
    file_list.append(current_leaf[0])    
    #print(my_leaf)

    for child in my_node.children:
        if(child.children is not None):
            #recursion needs to happen
            #print(f"recursion {counter}")
            file_list.extend(rec_props_to_html(child))
    
        #you need to convert the htmlnode to a leafnode to use .to_html()
        #leafnode: def __init__(self,tag,value, props=None):
        if(child.value is not None):
            my_leaf=LeafNode(child.tag, child.value, child.props)
            child_leaf=my_leaf.to_html()
            #print(f"{my_leaf!r}")
            file_list.append("".join(child_leaf))    
    file_list.append(current_leaf[1])
    return file_list
    
'''