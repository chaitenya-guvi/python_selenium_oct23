"""fromkeys
Creates key-value pairs from comma separated values:"""

dict1 = {}.fromkeys("a","b") # {'a': 'b'}
dict2 = {}.fromkeys(["email","phne_number"], None) # {'email': 'unknown'}  something as default values
dict3 = {}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}

print(f"the dict 1 is  : {dict1}")
print(f"the dict 2 is  : {dict2}")
print(f"the dict 3 is  : {dict3}")