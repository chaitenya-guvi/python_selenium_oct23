"""
global
Lets us reference variables that were originally assigned on the global scope
"""
total = 0

def increment():
    total += 1
    return total

increment() # Error!


"""

Correct way 
Lets us reference variables that were originally assigned on the global scope
"""
#
# total = 0
#
# def increment():
#     global total
#     total += 1
#     return total
#
#
# print(increment())