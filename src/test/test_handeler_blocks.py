import unittest
import inspect
from src.handeler_blocks import markdown_to_blocks, block_to_block_type, BlockType



#test markdown_to_blocks(text) 3 test
class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected=[
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,expected)
    
    
    def test_odd_input(self):
        text="""
     
 
     
1 item all other lines got spaces    
   
       
"""
        expected=["1 item all other lines got spaces"]
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks,expected)
    
    
    def test_markdown_to_blocks_Errors(self):
        with self.assertRaises(ValueError):
            markdown_to_blocks([])
        with self.assertRaises(ValueError):
            markdown_to_blocks("")
        with self.assertRaises(ValueError):
            markdown_to_blocks(None)
        with self.assertRaises(NotImplementedError):
            markdown_to_blocks("\n\n")

#test block_to_block_type(block_text)        
class test_block_to_block_type(unittest.TestCase):
    def test_return_heading(self):
        text="### fsdfs"
        expected=BlockType.HEADING
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="# fsdfs"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="###### f#s#d#f#s\n\n\n\n\n####\n###"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="#fsdfs"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text=" ##f#s#dfs"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="########f#s#dfs"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        

    def test_return_code(self):
        text="```### fsdfs```"
        expected=BlockType.CODE
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="``` ```"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="```###### f#s#d#f#s\n\n\n\n\n####\n###```"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="```"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="```fsdfsdf"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="?"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)   

    def test_return_quote(self):
        text="> abc"
        expected=BlockType.QUOTE
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="> ccc\n> bbb\n> aaa"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="> "
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="> aa\n>\n"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="> > > > > >"
        expected=BlockType.QUOTE
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="> 123\n"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        

    def test_return_unordered_list(self):
        text="- abc"
        expected=BlockType.UNORDERED_LIST
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="- a\n- b\n- c"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="- "
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="-"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="- \n- yes"
        expected=BlockType.UNORDERED_LIST
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="-\n"
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)

    def test_return_ordered_list(self):
        text="1. a"
        expected=BlockType.ORDERED_LIST
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="1. a\n2. b\n3. c\n4. \n5. \n6. \n7. \n8. \n9. \n10. \n11. "
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="1. "
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="1."
        expected=BlockType.PARAGRAPH
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)
        text="1. \n5. no"
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)        
        text="1. \n\n2. "
        blocks = block_to_block_type(text)
        self.assertEqual(blocks,expected)     

    def test_ValueError(self):
        with self.assertRaises(ValueError):
            block_to_block_type(None)
        with self.assertRaises(ValueError):
            block_to_block_type("")
        with self.assertRaises(ValueError):
            block_to_block_type([])
        with self.assertRaises(ValueError):
            block_to_block_type(BlockType.CODE)
        with self.assertRaises(ValueError):
            block_to_block_type([BlockType.CODE])
        