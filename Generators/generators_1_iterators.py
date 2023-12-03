"""
Iterators are methods that iterate collections like lists, tuples, etc.
Using an iterator method, we can loop through an object and return its elements.

Iterator - an object that can be iterated upon.
            An object which returns data, one element at a time when next() is called on it

Iterable -  An object which will return an Iterator when iter() is called on it.

"""

print("HELLO")
# is an iterable, but it is not an iterator.

print(iter("HELLO"))
#returns an iterator
# <str_iterator object at 0x000001D0DAAD7AC0>


