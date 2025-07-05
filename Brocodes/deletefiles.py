import  os
#you use import os module to interact with your operating system
# it works with file paths, list files and folders, check if a file exists, get environment variables,
# create or delete directories, delete files & empty folders

import shutil
#used for high level file operations
#helps copy files and folders, move files, delete entire folders that contains files , archive files (zip, tar, e.t.c)

source = "C:\\Users\\HP\Desktop\\folder"

try:
    shutil.rmtree(source) #this deletes a folder/directory containing a files
    print("Folder has been deleted!")
    #os.remove(source) only deletes files
# this function won't delete empty folders
    #os.rmdir(source) deletes an empty directory
# #this won't delete a folder that is not empty
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("You do not have permission to delete that")


