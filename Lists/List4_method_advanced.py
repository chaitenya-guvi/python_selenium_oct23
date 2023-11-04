"""
Using slicing to update a portion of list

"""

numbers = [1, 2, 3, 4, 5]
print(numbers[1:3])
numbers[1:3] = ['a','b','c']

print(numbers) # [1, 'a', 'b', 'c', 4, 5]
