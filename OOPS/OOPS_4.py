"""
self keyword
The self keyword refers to the current class instance.
self must always be the first parameter to __init__
and any methods and properties on class instances.


"""

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year