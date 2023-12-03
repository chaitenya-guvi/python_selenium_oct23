"""
Python reads files by using a cursor
This is like the cursor you see when you're typing
After a file is read, the cursor is at the end
To move the cursor, use the seek method
To read only part of a file, pass a number of characters into read, or use readline
To get a list of all lines, use readlines
"""

file_obj = open("text_example.txt") # relative path
# file_obj = open("C:\\Users\\LENOVO\\Desktop\\AT22\\File_handling\\text_example.txt")  # absolute path
# print(file_obj.read())
print(file_obj.readlines())

