class Dog:
    def sound(self):
        print("dog sound")

# Run-Time Polymorphism: Method Overriding


class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")


class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")

# Compile-Time Polymorphism: Method Overloading


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()


# Compile-Time Polymorphism
calc = Calculator()
print(calc.add(50, 10))
print(calc.add(50, 10, 20))
