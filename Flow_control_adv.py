# """
# 1. if you are 18  - adult
# 2. if you are 21 or above -- you can vote
# """
# # Nested if else block
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You can vote")
    elif age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult yet ! :(")
else:
    print("Please enter an age!")

"""
In Python, all conditional checks resolve to True or False.

Truthiness
x = 1
x is 1  # True
x is 0  # False
We can call values that will resolve to True "truthy", or values that will resolve to False "falsy".

Besides False conditional checks, other things that are naturally
falsy include: empty objects, empty strings, None, and zero.

"""

# number = {}
# print(bool(number))


