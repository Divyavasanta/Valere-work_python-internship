dict_1 = {"DV": 25, "AJ": 2, "VK": 15, "HR": 20, "AB": 30}
value = dict_1.setdefault("DV", 4)
print(dict_1)
print(value)
value = dict_1.setdefault('d', 5)
print(value)
print(dict_1)
