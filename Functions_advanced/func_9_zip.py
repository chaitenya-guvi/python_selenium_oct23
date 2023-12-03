"""
Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples,
where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

The iterator stops when the shortest input iterable is exhausted.

"""


first_zip = zip([1,2,3], [4,5,6])
print(first_zip)
# print(list(first_zip))
# [(1, 4), (2, 5), (3, 6)]

print(dict(first_zip))
# {1: 4, 2: 5, 3: 6}


"""
example 2
"""
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
#
print(list(zip(*five_by_two)))

