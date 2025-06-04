import json

data = {
    "Name": "Divya",
    "Age": 20,
    "City": "New York"
}

with open("output.json", "w", newline = '' ) as file:
    json.dump(data, file, indent = 4)
    
    