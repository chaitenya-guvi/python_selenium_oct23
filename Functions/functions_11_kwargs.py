"""
**kwargs
A special operator we can pass to functions

Gathers remaining keyword arguments as a dictionary

"""


def favorite_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


favorite_colors(rusty='green', Chaitenya='blue')

# rusty's favorite color is green
# Chaitenya's favorite color is blue


"""
Example 2 
"""


def special_greeting(**kwargs):
    if "Chaitenya" in kwargs and kwargs["Chaitenya"] == "special":
        return "You get a special greeting Chaitenya!"
    elif "Chaitenya" in kwargs:
        return f"{kwargs['Chaitenya']} Chaitenya!"
    return "Not sure who this is..."


special_greeting(Chaitenya='Hello')  # Hello Chaitenya!
special_greeting(Bob='hello')  # Not sure who this is...
special_greeting(Chaitenya='special')  # You get a special greeting Chaitenya!
