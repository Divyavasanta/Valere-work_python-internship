marks = {"Divya" : 25 , "Arpit" : 24 }
print(marks["Arpit"])
marks["Abhik"] = 20
print(marks["Abhik"])
for name, score in marks.items():
    print(name, "scored", score)
