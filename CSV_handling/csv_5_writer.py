"""
writer - creates a writer object for writing to CSV
writerow - method on a writer to write a row to the CSV
"""

from csv import writer
with open("fighter_game.csv", "w") as file_object:
    csv_writer = writer(file_object)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    csv_writer.writerow(["Ryu", "Hadouken"])
    csv_writer.writerow(["Ryu", "Hadouken"])