"""
Keyword Arguments
this is used to be more verbose .
"""

def full_name(first, last):
    return f"Your fname is {first} and lname is  {last}"


print(full_name('Chaitenya', 'Kumar'))
print(full_name(first='Chaitenya', last='Kumar'))
# Your name is Chaitenya Kumar

print(full_name(last='Kumar', first='Chaitenya'))