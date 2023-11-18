"""
List comprehension - shorthand method
the syntax
[____  for ____ in ____ ]
"""

# Looping
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []
#
# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)
#
# print(doubled_numbers) # [2, 4, 6, 8, 10]

# List Comprehension
#
# numbers_list = [1, 2, 3, 4, 5]
# doubled_numbers = [number * 2 for number in numbers_list]
# print(doubled_numbers) # [2, 4, 6, 8, 10]
#
#
#
# # Examples


# friends = ['ashley', 'matt', 'michael']

# upper_case_list = [friend.capitalize() for friend in friends]  # ['Ashley', 'Matt', 'Michael']
# print(upper_case_list)

#
# # example 2
# name = 'Chaitenya'
# print(name.upper())
# print([char.upper() for char in name])
# print(''.join([char.upper() for char in name]))
#
# # example 3
values = [0, [], '', None,1]
print([bool(val) for val in values]) #[False, False, False, False, True]

