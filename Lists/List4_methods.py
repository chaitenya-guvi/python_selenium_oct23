"""
Lists are mutable
"""
# list1 = list(range(8))
# print(list1)
# list1[0] = 'a'
# print(list1)


# """
# append
# Add an item to the end of the list.
# increases the length of the list
# """
# first_list = [1, 2, 3, 4]
# print(first_list)
# first_list.append(5)
# print(first_list)  # [1, 2, 3, 4, 5]
#



"""
extend
Add to the end of a list all values passed to extend

extend takes an iterable as argument
"""
#
# first_list = [1, 2, 3, 4]
# print(first_list)
# # first_list.append(5, 6, 7, 8)  # does not work!
# # first_list.append([5, 6, 7, 8])
# # print(first_list)  # [1, 2, 3, 4,  [5, 6, 7, 8]]  , length is 5
# correct_list = [1, 2, 3, 4]
# correct_list.extend([5, 6, 7, 8])
# print(correct_list)  # [1, 2, 3, 4, 5, 6, 7, 8] , length is 8

"""
insert
Insert an item at a given position
insert(index,element)
"""

first_list = [1, 2, 3, 4]
print(first_list)
first_list.insert(2, 'Hi!')

print(first_list) # [1, 2, 'Hi!', 3, 4]

# try to add an element at the end of the list
first_list.insert(-1, 'The end!')
print(first_list) # [1, 2, 'Hi!', 3, 'The end!', 4]


# first way to add element to end of list
first_list.append("the actual end")
print(first_list) #[1, 2, 'Hi!', 3, 'The end!', 4, 'the actual end']


# second way to add element to end of list
first_list.insert(len(first_list), 'The end using insert !')
print(first_list) #[1, 2, 'Hi!', 3, 'The end!', 4, 'the actual end', 'The end using insert !']
