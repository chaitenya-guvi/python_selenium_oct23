"""
Technically, a Python iterator object must implement two special methods
, __iter__() and __next__(), collectively called the iterator protocol.
"""


# define a list
my_list = [4, 7, 0] # iterable object

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0


"""
NOTE : When we reach the end and there is no more data to be returned,
        we will get the StopIteration Exception.
"""
#
# print(next(iterator))  # error
"""
For loop

for loop iterates over the elements of the iterator object.

On each iteration, the loop assigns the value of 
the next element to the variable element, and then executes the indented code block.
This process continues until the iterator is exhausted, at which point the for loop terminates.

"""
# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create an iterator from the list
iterator = iter(my_list)

# iterate through the elements of the iterator
for element in iterator:

    # Print each element
    print(element)