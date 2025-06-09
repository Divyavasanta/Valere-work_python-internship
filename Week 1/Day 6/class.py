class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = person("AJ", 40)
person2 = person("Dv", 20)

person1.info()
person2.info()
