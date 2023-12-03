"""
Reading
"""

numbers = {1, 2, 3, 4}

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4


# Q : how many unique characters are there in your name
name = "chaitenya"
characters = len(name)
char_in_name = set(name)
unique_characters = len(char_in_name)

print(char_in_name)



print(f"My name is  : {name} , the characters in my name is : {characters} , the unique ones are : {unique_characters}")
