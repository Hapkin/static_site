### how the recurrance works in to_html()
# child.to_html() will call the right occurrence as it is or a parent and will call it again or a leaf and then only return the string
#ABC makes sure you can't make an HTMLNode()


from abc import ABC, abstractmethod

#ABC =  abstract base class => it doesn't allow HTMLNodes to be created
class HTMLNode(ABC):
    def to_html(self):
        raise NotImplementedError()

class LeafNode(HTMLNode):
    def to_html(self):
        # return HTML leaf string
        ...

class ParentNode(HTMLNode):
    def to_html(self):
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"


