"""
The super() keyword allows us to call the __init__ function of a parent class
In the example below, we initialize the child with both its
own __init__ method and its parent's __init__ method:
"""

class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        super().__init__("canine")
        self.name = name

breed = Dog("Scooby")
print(breed.name)
print(breed.species)