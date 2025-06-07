

class HTMLNode():
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
    
    def to_html(self):
        raise NotImplementedError
    
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
    def __repr__(self):
        result=""
        if not (self.tag is None):
            result+=f"HTML: <{self.tag}>\n"
        if not (self.value is None):
            result+=f"text-inside: {self.value!r}\n"
        if not (self.children is None):
            result+=f"childnodes: {self.children!r}\n"
        if not (self.props is None):
            result+=f"Props:\n"
            props_string=", ".join(f"{key!r}: {value!r}" for key, value in self.props.items())
            result+=props_string
        
        return result
    
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