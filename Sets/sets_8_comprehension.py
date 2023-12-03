"""
Comprehension

"""

# Example 1 :

set1 = {x**2 for x in range(10)}
print(set1)
print(list(set1))


# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Example 2 :
def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

"""
Summary :
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""