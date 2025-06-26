from abc import ABC, abstractmethod

#ABC =  abstract base class => it doesn't allow HTMLNodes to be created
class HTMLNode(ABC):
    def __init__(self, tag=None, value=None, children=None,props=None):
        self.tag=tag                #string <a>
        self.value=value            #string the text inside a <p>paragraph</p>
        self.children=children    #list of HTMLNode [] ==>li's
        self.props=props            #dictionary {"href": "www.google.com"}

    '''
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
    '''
    
    #ABC =  abstract base class
    @abstractmethod
    def to_html(self):
        pass
        # raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return ""
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
            return result
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.children == other.children and 
                self.props == other.props)

    #def __repr__(self): => easier
    #    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"
    def __str__(self):
        result=""
        if (self.tag is not None):
            result+=f"HTML: <{self.tag}>\n"
        else:
            result+=f"HTML: N/A\n"
        if (self.value is not None):
            result+=f"text-inside: {self.value!r}\n"
        else:
            result+=f"text-inside: N/A\n"
        if (self.children is not None):
            child_types = ", ".join(type(child).__name__ for child in self.children)
            result += f"children ({len(self.children)}): [{child_types}]\n"
        else:
            result += f"no children found"
        if (self.props is not None):
            result+=f"Props:\n"
            props_string=", ".join(f"{key!r}:{value!r}" for key, value in self.props.items())
            result+=props_string
        
        return result
    
    def __repr__(self):
        return f"{type(self).__name__}{self.tag!r}, children={len(self.children) if self.children else 0})"
    
        '''
    def props_to_html(self):
        if ('href' in self.props.keys()): #er wordt nog geen rekening mee gehouden als target niet bestaat...
            result=f' href="{self.props.get('href')}" target="{self.props.get('target')}"'    
        else:
            return False
            #raise Exception("no 'href' found")
        return result
       #result href="https://www.google.com" target="_blank"
'''    