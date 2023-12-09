"""
1. Since a child class can inherit all the functionalities of the parent's class,
    this allows code reusability.
2. Once a functionality is developed, you can simply inherit it. No need to reinvent the wheel.
  This allows for cleaner code and easier to maintain.
3. Since you can also add your own functionalities in the child class,
   you can inherit only the useful functionalities and define other required features.
"""

class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()