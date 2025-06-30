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
    except ValueError as ve:
        print("%%%%%%%")
    except Exception as e:
        print(f"{path_delete} not empty")
        print(e.__traceback__)
        print(f"###\n{e}")
        try:
            for filepath in os.listdir(path_delete):
                combined=path_delete +"/{}".format(filepath)
                if(os.path.isdir(combined)):
                    delete_folder(combined)
                else:
                    os.remove(combined)
            os.rmdir(path_delete)
        except Exception as e:
            print(f"{e} ||ERROR ")
    #finally:

        


#copy files from static to public
def copy_folder_to_folder(path_from, path_to, attempt=0):
    #check if parameters are strings
    if(type(path_to)!=str and type(path_from)!=str):
        raise ValueError("delete_folder: expecting path to delete (str)")
    #check if first call then delete the directory first
    if attempt == 0:  # First call only
        if os.path.exists(path_to):
            shutil.rmtree(path_to)
            attempt+=1 #so it's no longer first call next recurrance
    
    #actual copying
    if not (os.path.exists(path_to)):
        os.mkdir(path_to)

    print(path_from, path_to, attempt)
    #shutil.copytree(path_from,path_to, dirs_exist_ok=True)
    for filepath in os.listdir(path_from):
        combined=path_from +"/{}".format(filepath)
        combined_to=path_to +"/{}".format(filepath)
        if(os.path.isdir(combined)):  #if is dir recurrance with the new paths
            os.mkdir(combined_to)
            copy_folder_to_folder(combined, combined_to, attempt)
        else: #else not a dir so copy with original paths
            shutil.copy(combined, combined_to)
    