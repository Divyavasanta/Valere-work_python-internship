class student:

    def __init__(self, *args):

        self.name = "None"
        self.age = "None"
        self.roll = "None"

        if len(args) == 1:
            self.name = args[0]

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.roll = args[2]

    def info(self):
        print(f"Name : {self.name}, age : {self.age} , roll : {self.roll})")


st1 = student("Dv")
st2 = student("Dv", 20)
st3 = student("Dv", 20, 211023)

st1.info()
st2.info()
st3.info()
