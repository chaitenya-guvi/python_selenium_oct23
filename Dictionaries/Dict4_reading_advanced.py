instructor = {
    "name": "Chaitenya",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

# for key, value in instructor.items():
#     print(f"{key} has this  value: {value}")

# name "Chaitenya"
# owns_dog True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number!"


# Does a dictionary have a value?
print("name" in instructor)
print("awesome" in instructor)
#
# # Does a dictionary have a key?
#
#
print("Chaitenya" in instructor.values())
print("Nope!" in instructor.values())
