"""An ordered collection or grouping of items!
But it is immutable!

interview question : What is the difference between a tuple and list ???
"""

numbers_tuple = (1, 2, 3, 4)
numbers_list = [1, 2, 3, 4]


"""
Immutable?
Can NEVER be changed!

"""

print(numbers_list)
numbers_list[0] = "change me!"
print(numbers_list)

"""trying to change index value in a tuple """
numbers_tuple[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

