from abc import ABC, abstractmethod


class Dog(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Species:Labrador, Sound: Woof!")


class Beagle(Dog):
    def sound(self):
        print("Species: Beagle, Sound : Bark!")


dogs = [Labrador("Fluffy"), Beagle("Sheru")]
for dog in dogs:
    dog.display_name()
    dog.sound()
