"""
CSV module

reader - lets you iterate over rows of the CSV as lists
DictReader - lets you iterate over rows of the CSV as OrderedDicts
Keys are determined by the header row
An OrderedDict is like a dictionary, but it remembers the order in which keys were inserted

"""
"""
reader

"""
from csv import reader
with open("fighters.csv") as file_object:
    csv_reader = reader(file_object)
    for row in csv_reader:
        # each row is a list!
        print(row)