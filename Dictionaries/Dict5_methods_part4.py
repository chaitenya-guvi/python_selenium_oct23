"""get
Retrieves a key in an object and return None instead of a KeyError if the key does not exist: """



d = dict(a=1, b=2, c=3)
# print(d)
# print(d['a'])
# d.get('a')  # 1
# d['b']  # 2
# d.get('b')  # 2
# print(d['no_key'])
print(d.get('no_key'))
