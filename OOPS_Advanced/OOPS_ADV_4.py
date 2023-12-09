"""
Polymorphism

A key principle in OOP is the idea of polymorphism -
an object can take on many (poly) forms (morph).

While a formal definition of polymorphism is more difficult,
 here are two important practical applications:
"""



"""
Exmple 1
 The same class method works in a similar way for different classes

Each subclass will have a different implementation of the method.
If the method is not implemented in the subclass,
    the version in the parent class is called instead.

Cat.speak()  # meow
Dog.speak()  # woof
Human.speak()  # yo
"""

"""
Exmple 2 
2. The same operation works for different kinds of objects
"""
sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

print(len(sample_list))
print(len(sample_tuple))
print(len(sample_string))