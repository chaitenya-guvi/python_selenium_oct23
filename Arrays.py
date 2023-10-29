# # indexing in python
# name = "Chaitenya"
# # syntax for accessing a specific index
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
# print(name[8])
# # print(name[-1])
# # print(name[-2])
# print(len(name))   # to check the length of any string

""" Slices
[start : stop : skip ]
start -   it is inclusive
stop  -   it is not inclusive
skip  -   jump by that specific integer value
"""
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alphabets))
# print(alphabets[26])
# print(alphabets[0])  # A
# print(alphabets[25])  # Z
print(alphabets[0:len(alphabets):2])
print(alphabets[::2])
# # print reverse
print(alphabets[::-2])
#
#
# palindrome_example = 'racecar'
# # interview question - check whether a string is palindrome or not
# print(palindrome_example == palindrome_example[::-1])

