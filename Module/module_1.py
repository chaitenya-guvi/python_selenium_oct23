"""
Keep Python files small
Reuse code across multiple files by importing
A module is just a Python file!

"""

"""
Built in 
"""
# import random
#
# print(random.choice(["apple", "banana", "cherry", "durian"]))
# list1 = ["apple", "banana", "cherry", "durian"]
# print(list1)
# random.shuffle(list1)
# print("After shuffle ")
# print(list1)
# ###########
"""changing the name while calling import """

# import random as omg_so_random
# #
# print(omg_so_random.choice(["apple", "banana", "cherry", "durian"]))
# omg_so_random.shuffle(["apple", "banana", "cherry", "durian"])

import random as r

print(r.choice(["apple", "banana", "cherry", "durian"]))
r.shuffle(["apple", "banana", "cherry", "durian"])
