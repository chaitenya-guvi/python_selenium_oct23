"""
clear
Remove all items from the list.
"""

# first_list = [1, 2, 3, 4]
#
# first_list.clear()
#
# print(first_list)  # []

"""
pop
Remove the item at the given position in the list, and return it.
If no index is specified, removes & returns last item in the list.
"""
# first_list = ['a', 'b', 'c', 'd']
# print(f"The original list is  : {first_list} ")
# popped_value = first_list.pop()  # 'd'
# print(f"This is the popped value :: {popped_value}")
# print(first_list)
# popped_value = first_list.pop(1)  # 'b'
# print(f"This is the popped value :: {popped_value}")
# print(first_list)

"""
remove
Remove the first item from the list whose value is x. 
Throws a ValueError if the item is not found.
"""

first_list = ['a', 'b', 'c', 'd','a']
first_list.remove('a')
print(first_list)  # ['b', 'c', 'd']
# first_list.remove(4)
# print(first_list)  # [1, 3, 4, 4]

"""
del 

Deletes a value from a list
"""

first_list = [1, 2, 3, 4]

del first_list[3]

print(first_list)  # [1, 2, 3]

del first_list[1]

print(first_list)  # [1, 3]
