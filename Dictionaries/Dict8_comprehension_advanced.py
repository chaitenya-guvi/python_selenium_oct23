"""
Conditional Logic

"""
num_list = [1,2,3,4]

print({num: ("even" if num % 2 == 0 else "odd") for num in num_list})

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}