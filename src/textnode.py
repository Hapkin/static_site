from enum import Enum


class TextType(Enum):    
    TEXT = ""       #"Normal text"
    BOLD = "**"       #"**Bold text**"
    ITALIC = "_"   #"_Italic text_"
    CODE = "`"       #"`Code text`"
    LINK = "a"       #"[anchor text](url)"
    IMAGE = "img"     #"![alt text](url)"



class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type= text_type #member of TEXT_TYPE enum
        else:
            raise ValueError(f"{text_type} != TextType.* :Raised in class(TextNode)")
        self.url = url
    
    def __eq__(self, other):
        if(self.text==other.text) and (self.text_type==other.text_type) and(self.url==other.url):
            return True
        
    def __repr__(self):
        if(self.url is None):
            return f"TextNode({self.text!r}, {self.text_type})"
        else:
            return f"TextNode({self.text!r}, {self.text_type}, {self.url!r})"
    

