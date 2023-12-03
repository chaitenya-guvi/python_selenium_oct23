"""
Sets are like formal mathematical sets.

Sets do not have duplicate values  -------- IMPORTANT

Elements in sets aren't ordered.

You cannot access items in a set by index.

Sets can be useful if you need to keep track of a collection of elements,
but don't care about ordering, keys or values and duplicates
"""

"""
Creating
"""

# Sets cannot have duplictes
set1 = set({1, 2, 3, 4, 5, 5, 5,5,5,5,5,5,5,5,5,5,5,5,6}) # {1, 2, 3, 4, 5}
print(set1)

set2 = {'a','b','c','c','c','c'}
print(set2)

# Creating a new set
# s = set({1, 4, 5})

# Creates a set with the same values as above
# s = {1, 4, 5}

print(4 in set1)
# True

print(8 in set1)
# False
