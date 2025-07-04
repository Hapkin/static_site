from src.handler_IO import copy_folder_to_folder
from src.generate_pages import generate_all_pages_static

def main():
    path_to_from="./static"
    path_to="./public"
    #delete_folder(path_to_del)
    copy_folder_to_folder(path_to_from,path_to)
    generate_all_pages_static()

    









main()