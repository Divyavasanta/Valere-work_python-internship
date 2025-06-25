import csv
with open(r"I:\Valere Internship\Week 1\Day 4\timezone.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
