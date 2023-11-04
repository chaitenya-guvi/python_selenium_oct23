tasks = ["Install Python", "Learn Python", "Take a break"]
List2 = ['a', True, 1, tasks, [1, 2, 3, 4,[5,6]]]  # heterogeneous data  , mutable

# for i in range(len(List2)):
#     print(f"The element is : {List2[i]}  and the type is : {type(List2[i])}")


"""
Accesing Nested list :
# Accesing a list within a list
"""
print(List2[3])  # ['Install Python', 'Learn Python', 'Take a break']
print(List2[3][-1])  # 'Take a break'

"""
Accessing nested list items 
"""
List3 = ['a', True, 1, tasks, [1, 2, 3, 4,[5,6,7]]]
print(List3[-1])
print(List3[-1][4])
print(List3[-1][4][-1])
