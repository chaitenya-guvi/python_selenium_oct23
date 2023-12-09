"""
Python Encapsulation
Encapsulation is one of the key features of object-oriented programming.
Encapsulation refers to the bundling of attributes and methods inside a single class.

It prevents outer classes from accessing and
changing attributes and methods of a class.
This also helps to achieve data hiding.

In Python, we denote private attributes using underscore
as the prefix i.e single _ or double __.

"""

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()