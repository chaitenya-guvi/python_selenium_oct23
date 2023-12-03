"""
A number is called abundant if the sum of all of its proper divisors exceeds the number.

Examples:

12 (1 + 2 + 3 + 4 + 6 > 12)
18 (1 + 2 + 3 + 6 + 9 > 18)
20 (1 + 2 + 4 + 5 + 10 > 20
"""
def is_abundant(n):
    total = 0
    for d in range(1,n):
        if n % d == 0:
            total += d
    return total > n


print(is_abundant(12))
print(is_abundant(4))
#
"""
List
"""
#
#
#
# def list_first_abundants(n):
#     abundant_nums = []
#     num = 1
#     while len(abundant_nums) < n:
#         if is_abundant(num):
#             abundant_nums.append(num)
#         num += 1
#     return abundant_nums
# #
# print(list_first_abundants(5))

"""
Generators
"""

def gen_first_abundants(n):
    count = 0
    num = 1
    while count < n:
        if is_abundant(num):
            yield num
            count += 1
        num +=1

iterator = gen_first_abundants(5)
print(next(iterator))
