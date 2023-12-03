"""
parameters
*args
default parameters
**kwargs
"""


def display_info(a, b, *args, instructor="Chaitenya", **kwargs):
  return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="Kumar", job="Instructor"))
#[1, 2, (3,), 'Chaitenya', {'job': 'Instructor', 'last_name': 'Kumar'}]