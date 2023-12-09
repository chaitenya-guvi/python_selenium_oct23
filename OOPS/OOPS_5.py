"""
Instance attributes and methods
Method - A Python Function defined inside a class is called a method.

Class Attributes

We can also define attributes directly
on a class that are shared by all instances
of a class and the class itself.

"""

class Person:
    first_name_default = "ABC"  # class attribute

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def class_method(cls):
        print("i am class method")

    def full_name(self):  # instance methods
        return f"My name is {self.first_name} {self.last_name}"

    def likes(self, thing):
        return f"{self.first_name} likes {thing}!"

p1 = Person("Chaitenya", "Kumar")
p2 = Person("Suba", "Kumar")
p3 = Person("Dinesh", "jain")

print(p1.full_name())
print(p2.full_name())
print(p3.full_name())

print(p1.first_name_default)
""" updating the class attribute for one object """
p1.first_name_default = "XYZ"
print(p1.first_name_default)
print(p2.first_name_default)
print(p3.first_name_default)

