"""
first_task = "Install Python"
second_task = "Learn Python"
third_task = "Take a break"
List can store heterogeneous data types also

CRUD - create , read , update , delete

tasks = []
ordered collection
creating a list ,reading lists ,  updting lists ,operations
"""

# []  - empty list , the paranthesis , block paranthesis
# each item is separated by a comma
# first_task = "Install Python"
# second_task = "Learn Python"
# third_task = "Take a break"
#
# # tasks = ["Install Python","Learn Python","Take a break"]
# # tasks2 = [first_task,second_task,third_task]
# # print(len(tasks2))

# list1 = [1,2,3,4,45236] # ist of inytegers
# list2 = ['a','b','c','d','e'] # list of strings
# list3 = [1, 'absdsds','b',2]  # mixed list

#
# # task is to create list of numbers from 1-10
# #
# numbers_list = list(range(1,10))
# print(numbers_list)
#
# print(f"{numbers_list[2]} is the third element in list ")

# friends = ["Ashley", "Matt", "Michael"]

# print(friends[0]) # 'Ashley'
# print(friends[2]) # 'Michael'
# print(friends[-1]) # last element in list
# print(friends[3]) # IndexError

# for name in friends :
#     print(f"{name} is a friend of mine , say hello ")
#
# # utilis in keyword to check whether an element exists in a list
#
# print("Ashley" in friends)
# print("Chaitenya" in friends)


# Accessing all elements in a list using while loop  :
numbers = [1, 2, 3, 4]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1



#
# # creating a list using range function
# range_of_number  = list(range(0,51,2))
# print(range_of_number)
#
# # accessing \ reading a list
#
# print(list3[2])
# print(list3[::-1])  # reversing a list
# print(list3[1:3])  # slicing a list , does not impact the original list
#
# # accessing \ reading a list using for loop
# for character in list2 :
#     print(character)
#
# # checking whether a vvalue is present in a list using in operator
# print('a' in list2 )
# print('aaa' in list2 )
#
# # length of a list
#
# # print(len(list1))
#
#
#
