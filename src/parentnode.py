from src.htmlnode import HTMLNode


#We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. 
# It's a node with no children. In this next example,
#True <p>This is a paragraph.</p>
#False! <p>This is a paragraph.<b>This is bold text.</b>This is the last sentence.</p> #<b> is the leaf

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        if(children is None):
            raise ValueError("ParentNode.childeren must have a value.")
        super().__init__(tag, children=children, props=props)
        
        
        

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and 
                self.children == other.children and 
                self.props == other.props)

    def to_html(self):
        if (self.children is None) :
            raise ValueError("missing children prop.")
        if(self.tag is None):
            raise ValueError("missing tag prop.")
        list_of_childs=rec_props_to_html(self)
        f"/n".join(list_of_childs)
        


## recursion_to_html
def rec_props_to_html(my_node):
    file_list = []
    for child in my_node:
        #you need to convert the htmlnode to a leafnode to use .to_html()
        #leafnode: def __init__(self,tag,value, props=None):
        if(child.value is None):
            my_leaf=child(child.tag, "", child.props)
        else:
            my_leaf=child(child.tag, child.value, child.props)
            file_list.append(my_leaf.to_html)    
        if(child.children is not None):
            #recursion needs to happen
            file_list.extend(rec_props_to_html(child))
    return file_list
