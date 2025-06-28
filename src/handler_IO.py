import os
import shutil


#delete all files public
def delete_folder(path_delete):
    if(type(path_delete)!=str):
        raise ValueError("delete_folder: expecting path to delete (str)")
    if not (os.path.exists(path_delete)):
        raise ValueError(f"Path is not found!: {path_delete}")
    try:
        os.rmdir(path_delete)
    except:
        print(f"{path_delete} not empty")
    finally:
        try:
            for filepath in os.listdir(path_delete):
                os.remove(path_delete +"\{}".format(filepath))
            os.rmdir(path_delete)
        except Exception as e:
            print(f"{e} ||ERROR ")


#copy files from static to public
def copy_folder_to_folder(path_from, path_to):
    pass