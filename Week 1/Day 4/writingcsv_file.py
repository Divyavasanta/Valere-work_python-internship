import csv

data =[
    ['Name', 'Age', 'City'],
    ['Divya', '20', 'New York']
]

with open("output.csv","w", newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)
