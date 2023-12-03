"""
CSV files are a common file format for tabular data
comma separated file
We can read CSV files just like other text files
Python has a built-in CSV module to read/write CSVs more easily

"""

with open("fighters.csv") as file:
    print(file.read())

