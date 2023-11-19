"""
Creatig a dictionary
Syntax
another_dictionary = dict(key = 'value')

"""


another_dictionary = dict(firstname="Chaitenya",lastname = "Kumar") # {'key': 'value'}
print(another_dictionary)
print(type(another_dictionary))

"""
Reading : 
"""
instructor = {
    "name": "Chaitenya",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

# print(instructor["name"])
# print(instructor[44])
#
# instructor["thing"] # KeyError