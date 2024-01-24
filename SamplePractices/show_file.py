#!/usr/bin/python3
'''program which will take the file name as the input from the user and 
    show the content of the file in the console.
'''
file_name = input("Enter file name: ")
fobj = open(file_name)
print(fobj.read())
fobj.close()
