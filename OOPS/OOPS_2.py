"""
Abstraction - exposing only "relevant" data in a class interface,
    hiding private attributes and methods (aka the "inner workings") from users
"""


class Vehicle:

    def __init__(self, make, model, year): #method constructor
        self.make = make
        self.model = model
        self.year = year


"""
Classes in Python can have a special __init__ method, 
which gets called every time you create an instance of the class (instantiate).
It is also called constructor of class 
"""