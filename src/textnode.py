from enum import Enum


class TextType(Enum):    
    TEXT = ""       #"Normal text"
    BOLD = "**"       #"**Bold text**"
    ITALIC = "_"   #"_Italic text_"
    CODE = "`"       #"`Code text`"
    LINK = "a"       #"[anchor text](url)"
    IMAGE = "img"     #"![alt text](url)"

class ReMatches():
    def __init__(self, posxy, group1):
        self.x=posxy[0]
        self.y=posxy[1]
        self.group=group1

    def __str__(self):
        if(self.x is not None )and(self.y is not None)and (self.group is not None):
            return (f"pos: {self.x},{self.y} || {self.group}")

    


class TextNode():
    def __init__(self, text, text_type, url=None, IB=None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type= text_type #member of TEXT_TYPE enum
        else:
            raise ValueError(f"{text_type} != TextType.* :Raised in class(TextNode)")
        self.url = url
        self.IB=IB
    
    def __eq__(self, other):
        if(self.text==other.text) and (self.text_type==other.text_type) and(self.url==other.url):
            return True
        
    def __repr__(self):
        result=f"TextNode({self.text!r}, {self.text_type})"
        if(self.url is not None):
            result+=f", {self.url!r})"
        if(self.IB is not None):
            result+=f", {self.IB!r})"
        return result
    

