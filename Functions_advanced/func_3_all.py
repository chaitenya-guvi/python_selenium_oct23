"""
Return True if all elements of the iterable are truthy (or if the iterable is empty)
"""

print(all([ 0,1, 2, 3]))

print(all([char for char in 'eio' if char in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
