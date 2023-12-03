"""
We can use * as an argument to a function to "unpack" values
Unpacking the values
"""


def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)


list1 = [1, 2, 3, 4]
# sum_all_values(list1) # nope...
# sum_all_values((1, 2, 3, 4)) # this does not work either...
#
print(sum_all_values(*list1))
# sum_all_values(*(1, 2, 3, 4)) # 10