"""pop
Takes a single argument corresponding to a key and
removes that key-value pair from the dictionary.
Returns the value corresponding to the key that was removed."""


d = dict(a=1,b=2,c=3)
d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
d # {'c': 3, 'b': 2}
d.pop('e') # KeyError
