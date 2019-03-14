import os

def list_directory_content(path):
    path = os.path.abspath(path)
    for file in os.listdir(path):
        file_absolute_path = "{}\{}".format(path,file)
        print(file_absolute_path)
        if os.path.isdir(file_absolute_path):
            list_directory_content(file_absolute_path)

list_directory_content("./")