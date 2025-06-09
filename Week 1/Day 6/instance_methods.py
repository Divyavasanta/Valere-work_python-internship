class Cars:

    def __init__(self, brand="Safari", colour="pink"):
        self.brand = brand
        self.colour = colour

    def info(self):
        print(f"(brand name:{self.brand}, colour:{self.colour})")


car1 = Cars()
car2 = Cars("Fortuner", "black")

car1.info()
car2.info()
