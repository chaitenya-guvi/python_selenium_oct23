"""
a generator is a function that returns an iterator
that produces a sequence of values when iterated over.

Generators are iterators
Generators can be created with generator functions
NOTE  - Generator functions use the yield keyword


Generators are useful when we want to produce a large sequence of values,
but we don't want to store all of them in memory at once.
"""

"""
Syntax : 

def generator_name(arg):
    # statements
    yield something
    
    
Here, the yield keyword is used to produce a value from the generator.    
"""

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(100):
    # print each value produced by generator
    print(value)



