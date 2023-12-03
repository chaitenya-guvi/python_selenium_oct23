"""
You can close a file with the close method
You can check if a file is closed with the closed attribute
Once closed, a file can't be read again
Always close files - it frees up system resources!

"""

file_object = open("story.txt")
print(f"is the file object closed : {file_object.closed} ")

print(file_object.read())

file_object.close()


print(f"is the file object closed now ?   : {file_object.closed}")
