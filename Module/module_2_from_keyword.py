"""
- The from keyword lets you import parts of a module
    Handy rule of thumb: only import what you need!
- If you still want to import everything, you can also use the from MODULE import * patternThe from keyword lets you import parts of a module
    Handy rule of thumb: only import what you need!
If you still want to import everything, you can also use the from MODULE import * pattern
"""

# import random
# import random as omg_so_random
# from random import *
# from random import choice, shuffle
from random import choice as gimme_one, shuffle as mix_up_fruits



list1 = ["apple", "banana", "cherry", "durian"]
print(list1)
print(f"this is a random fruit from the list : {gimme_one(list1)}")