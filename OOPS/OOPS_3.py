"""
Instantiating
Creating an object that is an instance of a class is called instantiating a class.


Here, __init__() is the constructor function
that is called whenever a new object of that class is instantiated.
If we use a constructor to initialize values inside a class,
 we need to pass the corresponding value during the object creation of the class
"""
class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

v1 = Vehicle("Honda", "Civic", 2017)
v2 = Vehicle("Maruti","Ertiga",2020)


print(v1)  #<__main__.Vehicle at 0x10472f5c0>
print(v1.make) #'Honda'
print(v2.make) #Maruti
print(v1.model) #'Civic'
print(v1.year) #2017