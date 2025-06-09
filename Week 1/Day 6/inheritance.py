class Cat:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Cat's name is: {self.name}")

# single inheritance:


class PersianCat(Cat):

    def sound(self):
        print("Meow! I am a Persian cat.")

# multilevel inheritance:


class companionship(PersianCat):

    def companion(self):
        print("I am a great companion!")

# multiple inheritance:


class friendly:
    def greet(self):
        print("Hello! I am a friendly cat.")


class FriendlyPersianCat(PersianCat, friendly):
    def friendly_sound(self):
        print("Purr! I am a friendly Persian cat.")


l1 = PersianCat("Luna")
l1.display_name()
l1.sound()

companion_cat = companionship("Max")
companion_cat.display_name()
companion_cat.companion()

friendly_cat = FriendlyPersianCat("Leo")
friendly_cat.display_name()
friendly_cat.greet()
friendly_cat.friendly_sound()
