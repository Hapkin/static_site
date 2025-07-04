from src.handeler_html import markdown_to_html_node, check_html
from src.handler_IO import write_html_toFile, read_file, read_files_in_folder



def generate_all_pages_static():
    content=read_files_in_folder("content/")
    for item in content:
        public=item.replace("content","public")
        public=public.replace("md","html")
        generate_page(item,"template.html",public)
        print(f"making: {item} to {public}")
        

def extract_title(md):
    md.strip()
    if(not isinstance(md, str)) or not (md.startswith("# "))or (len(md)<3):
        print(f"{not isinstance(md, str)}or {not (md.startswith('# '))}or {(len(md)<3)}")
        raise ValueError("exctract_title: wrong value input")
    else:
        title=md[2:]
        return title

    

        

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    
    # split title from 'from_path'
    read_from= read_file(from_path)
    text_from=read_from.split("\n",1)
    title=extract_title(text_from[0])
    ##this is both title but also h1 tag!
    text_from=read_from
    
    
    # convert to html (nodes -> .to_html())
    htmlnodes_from=markdown_to_html_node(text_from)
    html_from=htmlnodes_from.to_html()
    
    
    #read template (this is already html!)
    html_template=read_file(template_path.strip())    
    
    #check html template lots of () because 1 of the OR's has to be true AND the .endswith has to be true
    if (check_html(html_template)):
        raise ValueError(f"generate_page(html_template): incorrect format; expect full <html> page.\n {html_template.split('\n', 1)[0]}")
    
    #replace Title and Content
    html=html_template.replace('{{ Title }}', title)
    html=html.replace('{{ Content }}', html_from)
    
    write_html_toFile(dest_path, html)