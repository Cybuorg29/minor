import os

def create_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    except OSError:
        print("Error creating directory")
        
create_folder("my_folder")