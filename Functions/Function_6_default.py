"""
Default values
Allows you to be more defensive
Avoids errors with incorrect parameters
More readable examples!
"""
# example 1
# def add(number1='please ', number2='pass a number instead'):
#     return number1+number2
#
# print(add())
# # print(add())
# print(add(5, 10))

"""# example 2 : """
def show_information(first_name="Chaitenya", is_instructor=False):
    if first_name == "Chaitenya" and is_instructor:
        return "Welcome back instructor Chaitenya!"
    elif first_name == "Chaitenya":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"


# print(show_information())
print(show_information(is_instructor=True)) # "Welcome back instructor Chaitenya!"
# print(show_information('Molly'))# Hello Molly!