"""
Normal functions have names.
Interview questuon :: difference between lamdas and functions  ? ???
"""

def first_function():
    """
    normal document
    :return: None
    """
    return 'Hello! i am a function'

#
# print(first_function())
# list1 = [1,2,3]
# print(type(list1))
# print(list1.__len__())
#
# print(first_function.__doc__)
# print(first_function.__name__)


"""
But lambdas are anonymous functions
"""

#
first_lambda = lambda x,y: x + 5+ y # shorthand expression
second_name = lambda a : a/2

print(second_name(200))
print(second_name.__name__)

# def function1(x,y) :
#     return x + 5 + y
#
print(first_lambda(10,15))
print(first_lambda(9,13))

print(first_lambda.__name__) # <lambda>