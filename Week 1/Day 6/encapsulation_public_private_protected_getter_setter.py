class Car:

    def __init__(self, name, brand, colour):
        self.name = name  # public attribute
        self._brand = brand  # protected attribute
        self.__colour = colour  # private attribute

    def get_info(self):
        return f"Car Name: {self.name}, Brand: {self._brand}, Colour: {self.__colour}"

    # Getter and Setter for private for private attribute

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        if colour in ["red", "blue", "black"]:
            self.__colour = colour
        else:
            print("Invalid colour. Colour must be red, blue, or black.")


car_1 = Car("Creta", "Hyundai", "red")
print(car_1.name)
print(car_1._brand)

print(car_1.get_colour())
car_1.set_colour("grey")
print(car_1.get_info())
