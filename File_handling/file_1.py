"""
You can read a file with the open function

open returns a file object to you

You can read a file object with the read method
The default mode is 'rt'
buffer , intermediate

Steps ;

1. Open the file using open() , save the content inside a file_object
2. Read the file_object using read()


"""

file_content = open("story.txt")  # return you a stream of objects .
# print(file_content)
# print(type(file_content))
print(file_content.read())
