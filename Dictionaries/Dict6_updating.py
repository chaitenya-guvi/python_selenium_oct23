"""
Update  :
Update keys and values in a dictionary with another set of key value pairs.
"""

first = dict(a=1,b=2,c=3,d=4,e=5)
print(first)
second = {} # empty dictionary
print(second)
#
second.update(first)
print(second)
print(second is first)
#
# # let's overwrite an existng key
second['a'] = "AMAZING"
print(second)
#
# # if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # the update overrides our values
print(second)
#
