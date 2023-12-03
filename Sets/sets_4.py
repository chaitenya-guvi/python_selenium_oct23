"""
remove

removes a value from the set - returns a KeyError if the value is not found

if you need to avoid KeyErrors use .discard()
"""

set1 = {1,2,3,4,5,6}

set1.remove(3)

print(set1) # {1, 2, 4, 5, 6}