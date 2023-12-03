"""
with block

automatically closes the file after use
indentation is needed

"""

with open("story.txt") as file_object :
    print(f"is the file object closed : {file_object.closed} ")
    print(file_object.read())


print(f"is the file object closed now ?   : {file_object.closed}")