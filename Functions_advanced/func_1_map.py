"""
A standard function that accepts at least two arguments, a function and an "iterable"

iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

runs the lambda for each value in the iterable and returns a map object which can be converted
 into another data structure
"""

# list1 = [1, 2, 3, 4]
#
# doubles = map(lambda x: x * 2 , list1)
# print(doubles)
#
# print(list(doubles))




"""
example 2 
"""
#
names = [
    {'first':'Rusty', 'last': 'Steele'},
    {'first':'CK', 'last': 'Steele', },
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))
#
print(first_names)
# ['Rusty', 'CK', 'Blue']