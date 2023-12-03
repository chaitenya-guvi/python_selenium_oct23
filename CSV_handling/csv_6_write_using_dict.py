"""
DictWriter - creates a writer object for writing using dictionaries
fieldnames - kwarg for the DictWriter specifying headers
writeheader - method on a writer to write header row
writerow - method on a writer to write a row based on a dictionary
Writing CSV Files Example

Using Dictionaries


"""

from csv import DictWriter
with open("example_write.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({ "Character": "Ryu", "Move": "Hadouken"})
    csv_writer.writerow({ "Character": "New", "Move": "punch"})