"""
Using ** as an Argument:

Dictionary Unpacking


"""

def display_names(first, second):
    return f"{first} says hello to {second}"


names = {"first": "Chaitenya",'second': "Rusty"}

# display_names(names)  # nope..

print(display_names(**names))
#"Chaitenya says hello to Rusty"
