from src.handler_IO import copy_folder_to_folder
from src.generate_pages import generate_all_pages_static
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    path_to_from="./static"
    path_to="./docs"
    #delete_folder(path_to_del)
    copy_folder_to_folder(path_to_from,path_to)
    build_from="content/"
    build_to="docs/"

    generate_all_pages_static(build_from,build_to, basepath)



main()