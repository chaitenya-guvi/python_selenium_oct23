"""
add
Adds an element to a set.
If the element is already in the set, the set doesn't change:

"""

s = set([1, 2, 3])

print(s)
s.add(4)
print(s)

s # {1, 2, 3, 4}

s.add(4)
print(s)
s # {1, 2, 3, 4}