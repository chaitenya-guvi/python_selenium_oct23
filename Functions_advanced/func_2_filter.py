"""
filter
There is a lambda for each value in the iterable.

Returns filter object which can be converted into other iterables

The object contains only the values that return true to the lambda
"""

list1 = [1,2,3,4,5,6,7,8]

evens = list(filter(lambda x: x % 2 == 0, list1))

print(evens)