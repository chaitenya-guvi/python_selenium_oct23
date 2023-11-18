"""
index :
returns the index of the specified item in the list
Can specify start and end

"""

# # # can specify start and stop
numbers = [5, 5, 6, 7, 5, 8,'a', 8, 9, 10]
# print(numbers.index('a')) # 6
# print(numbers.index(5, 1)) # 1
# print(numbers.index(5, 2)) # 4
# print(numbers[6:8])
# print(numbers.index('a', 6, 8)) # 6)
# # print(numbers[6:9])
# # print(numbers.index(10, 6, 9)) # )
#

"""
count
syntax : lisname.count(x)
return the number of times x appears in the list
"""

#
# numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2,1]
# print(len(numbers))
# print(numbers.count(2))
# print(numbers.count(21))
# print(numbers.count(3))



"""
reverse
 - reverses in place
 
"""

# first_list = [1, 2, 3, 4]
# # print(first_list[::-1])


# print(f"The original list is {first_list}")
# first_list.reverse()  # reverses in place
# print(f"The updated list is {first_list}")
# print(first_list) # [4, 3, 2, 1]


# print(list(reversed(first_list)))
# print(f"The original list is {first_list}")

"""
sort 
sort the items of the list (in-place)
"""
# another_list = [6, 4, 1, 2, 5]
# another_list = ['a','b','e','d']
#
# print(f"The original list is {another_list}")
#
# another_list.sort()
# print(f"The updated list is {another_list}")

#
# print(another_list) # [1, 2, 4, 5, 6]


"""
 join method
# technically a String method that takes an iterable argument
# concatenates (combines) a copy of the base string between each item of the iterable
# returns a new string 
"""
#
words = ['Coding', 'Is', 'Fun!']

print(' '.join(words)) # 'Coding is Fun!'
print(' #-++++ '.join(words)) # 'Coding #-++++ Is #-++++ Fun!'
print(''.join(words)) # 'CodingIsFun!'