from enum import Enum

class TextType(Enum):    
    TEXT = "text"   #"Normal text"
    BOLD = "bold"       #"**Bold text**"
    ITALIC = "italic"   #"_Italic text_"
    CODE = "code"       #"`Code text`"
    LINK = "link"       #"[anchor text](url)"
    IMAGE = "image"     #"![alt text](url)"



class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type= text_type #member of TEXT_TYPE enum
        self.url = url
    
    def __eq__(self, other):
        if(self.text==other.text) and (self.text_type==other.text_type) and(self.url==other.url):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    