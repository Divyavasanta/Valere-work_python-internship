import csv

with open(r"I:\Valere Internship\Week 1\Day 4\country.csv") as file:
    lines = file.readlines()


header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]


print("Columns :", header)

print("Number of records :", len(data))

print("\nParsed data:")
for row in data:
    print(row)

with open("I:\Valere Internship\Week 1\Day 4\country.csv", "a") as file:
    file.write("\nIndia, 1.4 billion, New Delhi\n")
