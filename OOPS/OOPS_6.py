"""
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
        return "i am class method"

    def full_name(self):  # instance methods
        return f"My name is {self.first_name} {self.last_name}"

    def likes(self, thing):
        return f"{self.first_name} likes {thing}!"

p1 = Person("Chaitenya", "Kumar")
p2 = Person("Suba", "Kumar")
p3 = Person("Dinesh", "jain")

# instance methods
print(p1.likes("ice cream"))
print(p2.likes("chocolates"))
print(p3.likes("juicess"))

# class method
print(p1.class_method())
print(p2.class_method())
print(p3.class_method())