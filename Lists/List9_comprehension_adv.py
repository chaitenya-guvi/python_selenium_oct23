"""LC with Conditional Logic


the syntax
[____  for ____ in ____]

"""

numbers = [1, 2, 3, 4, 5, 6]
#
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
#
# odds = [num for num in numbers if num % 2 != 0]
# print(odds)
#
# # example 2
# print([num * 2 if num % 2 == 0 else num * 3 for num in numbers])
#
# # example 3 - remove the vowels
# with_vowels = "This is so much fun!"
#
# print(''.join(char for char in with_vowels if char not in "aeiou"))

# "Ths s s mch fn!"
#
# # example 4 - nested LC
#
# board = [[num for num in range(1, 4)] for val in range(1, 4)]
# #
# print(board)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# # example 5 - nested LC
#
print([["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)])

# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
