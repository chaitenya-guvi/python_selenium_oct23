"""
Common mistakes in return statement
1. returning early in loop

"""

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in range(numbers+1):
#         if num % 2 != 0:
#             print(f"This is the odd number  : {num}")
#             total += num
#
#         return total
#
#
# print(sum_odd_numbers(6))

"""
un necessary else:
"""
# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     else:
#         return False


# print(is_odd_number(5))
#
#
def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

#
print(is_odd_number())