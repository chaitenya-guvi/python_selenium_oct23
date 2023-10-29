"""
# # concatenation  -  using the + operator
# # formatting -
#   f string - youtube video of fstring
"""

string1 = "hello"
firstname = "Priyanka"
secondname = "good morning"

greeting_name = string1 + ' ' + firstname + "," + secondname  # added three strings here
print(greeting_name)
"""
syntax is  
string then the '.' operator , then the method and the parenthesis
    example_string.example_method(arg1,arg2..)
 
"""
greeting_name2 = "{} {},{}".format(string1,firstname,secondname)
print(greeting_name2)
# greeting_name3 = "{2} {0},{1}".format(string1,firstname,secondname) # postion formatting
# print(greeting_name3)


greeting_name3_fstring = f"line 25 :  {string1} {firstname},{secondname}"
print(greeting_name3_fstring)

