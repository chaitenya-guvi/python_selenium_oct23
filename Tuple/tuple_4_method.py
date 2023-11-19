"""
count

Returns the number of times a value appears in a tuple:
"""
x = (1,2,3,3,3,3)
print(x.count(1))
print(x.count(3))


"""
index

Returns the index at which a value is found in a tuple.
"""

tuple1 = (1,2,3,3,3)
print(tuple1.index(1))
# 0
print(tuple1.index(5))
# ValueError: tuple.index(x): x not in tuple
print(tuple1.index(3))
# 2 - only the first matching index is returned