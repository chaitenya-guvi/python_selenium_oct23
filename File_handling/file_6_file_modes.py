"""
Modes for Opening Files

r - Read a file (no writing) - this is the default
w - Write to a file (previous contents removed)
a - Append to a file (previous contents not removed)
r+ - Read and write to a file (writing based on cursor)

"""


with open(file="haiku_2.txt",mode="w") as file_object:
    file_object.write("Writing files is great\n")
    file_object.write("Here's another line of text\n")
    file_object.write("Closing now, goodbye!\n")
    file_object.write("Closing now, goodnight!")

with open(file="haiku_2.txt",mode = 'a') as file_object :
    file_object.writelines(["\nHello this is  new 5th line ","\nthis is the sixth line"])