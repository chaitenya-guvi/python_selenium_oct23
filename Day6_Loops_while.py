"""
while
while loop we can execute a set of statements as long as a condition is true.
# """
# item = 1  # initialization
# while item < 6: # condition
#   print(item)
#   item += 1    #iteration


# infinite loop
# item = 5  # initialization
# while item < 6: # condition
#   print(item)
#       #iteration

#
# # break keyword
# # With the break statement we can stop the loop even if the while condition is true:
# item = 1
# while item < 10:
#   print(item)
#   if item == 3:
#     break
#   item += 1



# continue :
# With the continue statement we can stop the current iteration, and continue with the next:

# program to print odd numbers from 1 to 10

num = 0

while num < 10:
  num += 1
  if num  == 3 or num == 7 or num == 9:
    # print("it is is either 3 , 5, 7 , 9")
    continue
  print(num)


# pass statement  - tatement is a null statement which can be used as a placeholder for future code.
num = 0

while num < 10:
  num += 1
  if num  == 3 or num == 7 or num == 9:
    # print("it is is either 3 , 5, 7 , 9")
    # write the code later 
    pass
  print(num)