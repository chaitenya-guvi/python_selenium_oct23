"""
Inheritance
A key feature of OOP is the ability to define a class which
 inherits from another class (a "base" or "parent" class).

The new class that is created is known as subclass (child or derived class)
 and the existing class from which
the child class is derived is known as superclass (parent or base class)

In Python, inheritance works by passing the parent
class as an argument to the definition of a child class:

"""


"""
# parent class , super class , base class
"""
class Animal:
    def make_sound(self, sound):
        print(sound)

    cool = True

"""# child class , sub class , inheriting from the super class"""
class Cat(Animal):
    pass

class Dog(Animal):
    pass

gandalf = Cat()
gandalf.make_sound("meow")  # meow
print(gandalf.cool) # True

scooby = Dog()
scooby.make_sound("bark")
print(scooby.cool)


"""
Syntax : 

# define a superclass
class super_class:
    # attributes and method definition

# inheritance
class sub_class(super_class):
    # attributes and method of super_class
    # attributes and method of sub_class
"""