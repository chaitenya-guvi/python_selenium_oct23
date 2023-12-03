"""
You can also use open to write to a file
Need to specify the "w" flag as the second argument
"""
with open(file="haiku.txt",mode="w") as file_object:
    file_object.write("Writing files is great\n")
    file_object.write("Here's another line of text\n")
    file_object.write("Closing now, goodbye!\n")
    file_object.write("Closing now, goodnight!")