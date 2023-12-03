"""
*args
A special operator we can pass to functions

Gathers remaining arguments as a tuple
when t use : when you have variable length of arguments

This is just a parameter - you can call it whatever you want!
"""

# def my_function(*kids):
#   print(type(kids))
#   print("The youngest student  is " + kids[3])
#
# my_function("Robin", "Tobias", "Star","Aravind","Suba")

"""
Example 2
"""

def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total


print(sum_all_values(1, 2, 3))
print(sum_all_values(1, 2, 3, 7, 8, 8, 9))
#
print(sum_all_values(1, 2, 3, 4, 5))