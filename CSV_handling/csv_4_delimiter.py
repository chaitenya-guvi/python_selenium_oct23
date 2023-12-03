'''
delimiter
'''

from csv import reader
with open("example.csv") as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        # each row is a list!
        print(row) 