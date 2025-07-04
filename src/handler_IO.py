import os
import shutil
from src.handeler_html import check_html



#delete all files public
def delete_folder(path_delete):
    if(type(path_delete)!=str):
        raise ValueError("expecting path to delete (str)")
    if not (os.path.exists(path_delete)):
        raise ValueError(f"Path is not found!: {path_delete}")
    try:
        os.rmdir(path_delete)
    except ValueError as ve:
        print(f"delete_folder: {ve}")
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
            print(f"delete_folder: {e} ||ERROR ")
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
    

     
def create_dirs(dir):
    dirs= dir.split("/")
    #print(f"dirs: {dirs}")
    my_dir=""
    for i in range(0,len(dirs)):
        my_dir +=dirs[i]+"/"
        if not (os.path.exists(my_dir)):
            #print(f"creating 1: {my_dir}")
            os.mkdir(my_dir)
        else:
            #deze bestaat al dus moeten we die aan de rest toevoegen 
            #print(f"deze bestaat al || {my_dir}")
            pass
            
         

#extra function to write the html-page to dest_path
def write_html_toFile(dest_path, html):
    if not isinstance(dest_path, str)and not (check_html(html)):
        raise ValueError(f"write_html_toFile: arguments not right type.{dest_path}; {html.split('\n', 1)[0]}")
    
    dest_dir= os.path.dirname(dest_path)
    if not (os.path.exists(dest_dir)):
        create_dirs(dest_dir)
    
    #option w= create, or overwrite
    with open(dest_path, "w") as f:
        f.write(html)


def read_file(path):
    if not isinstance(path, str):
        raise ValueError(f"not a string: {path}")
    if not (os.path.exists(path)):
        raise ValueError(f"File not found: {path}")
    with open(path) as f:
        return f.read()
    
def read_files_in_folder(path):
    list_files=[]
    for item in os.listdir(path):
        new_path= path+ item
        if (os.path.isdir(new_path)):
            new_path=new_path+"/"
            #print(f"next:{new_path}")
            list_files.extend(read_files_in_folder(new_path))
        else:
            list_files.append(new_path) 
            
    #list_files += [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return list_files