'''4. Write a python program to print the contents of a directory using the os module. Search
online for the function which does that.'''

import os

# specify the directory path
path = "."  # current directory, you can change it to any directory you want

# print all files and folders in the directory
contents = os.listdir(path)

for item in contents:
    print(item)