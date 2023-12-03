"""
any
Return True if any element of the iterable is truthy.
If the iterable is empty, return False.
"""

print(any([0, 1, 2, 3]))

print(any([val for val in [1, 2, 3] if val > 2]))

print(any([val for val in [1, 2, 3] if val > 5]))