List1 = [1, 2, 3, 4]  # -- every datatype in list is same
# 0,1,2,3
tasks = ["Install Python", "Learn Python", "Take a break"]

List2 = ['a', True, 1, tasks, [1, 2, 3, 4]] # heterogeneous data  , mutable

# print(List1[2])
# print(type(List1[2]))
# print(tasks[2])
# print(type(tasks[2]))

# print(len(List2))

#
for i in range(len(List2)):
    print(f"The element is : {List2[i]}  and the type is : {type(List2[i])}")
