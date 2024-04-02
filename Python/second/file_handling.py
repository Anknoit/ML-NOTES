# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:03:40 2020

@author: CG-DTE
"""

f = open("read.txt", "r")   #"r" = Read

print(f.read())
print(f.readline()) #For printing firstline
print(f.readline()) #For printing seconline and so on.......
f.close()           #Closing files is a good habit

'''
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
    - It overwrite whole fuckin text file /USE IT CAREFULLY/
'''

def writenewline_func():
    f = open("read.txt", "a")
    f.write("One new line using append")
writenewline_func()

def write_overwrite():
    f = open("overwrite.txt", "x")
    f = open("overwrite.txt", "w")  #Initialtext = Hello Ankit
    f.write("I overwrite Hello ankit coz I used w")
write_overwrite()


'''
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
'''



