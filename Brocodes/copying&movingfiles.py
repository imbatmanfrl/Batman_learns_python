#import shutil

#shutil.copyfile("test.txt","copy2.txt")

import os

source = "Folder"
destination = "C:\\Users\\HP\Desktop\\Folder"

try:
    if os.path.exists(destination):
        print("There is already a file here ")
    else:
        os.replace(source,destination)
        print(source +" was moved")

except FileNotFoundError:
    print(source +" was not found")



