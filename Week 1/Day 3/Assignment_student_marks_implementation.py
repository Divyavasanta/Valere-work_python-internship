students = {}

def add_student():
   name = input("Enter student name: ")
   if name in students:
      print("This student name already exists.")
    else:
      marks = int(input("Enter student marks: "))
      students[name] = marks
      print(name + " added with marks " + str(marks) + ".")


