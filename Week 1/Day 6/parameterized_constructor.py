class Girls:

    def __init__(self, behaviour, workethics):
        self.behaviour = behaviour
        self.workethics = workethics


f1 = Girls("good", "excellent")
f2 = Girls("bad", "poor")

print("behaviour of f1 :{}".format(f1.behaviour))
print("workethics of f1 :{}" .format(f1.workethics))
print("behaviour of f2:{}".format(f2.behaviour))
print("workethics of f2:{}" .format(f2.workethics))
