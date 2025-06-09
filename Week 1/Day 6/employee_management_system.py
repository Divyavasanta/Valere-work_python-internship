class Employee:
    employee_count = 0

    def __init__(self, department, employee_id, salary):
        self.department = department
        self.employee_id = employee_id
        self.__salary = salary
        Employee.employee_count += 1

    def display(self):
        print(
            f"Department: {self.department}, Employee_ID: {self.employee_id}, Salary: {self.__salary}")

    def calculate_bonus(self):
        return self.__salary * 0.10

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary. Salary must be a positive number.")

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


class Developer(Employee):
    def __init__(self, department, employee_id, salary, language):
        super().__init__(department, employee_id, salary)
        self.language = language

    def calculate_bonus(self):
        return 0.15 * self.get_salary()

    def display(self):
        super().display()
        print(f"Role: Developer, Language: {self.language}")


class Manager(Employee):
    def __init__(self, department, employee_id, salary, team_size):
        super().__init__(department, employee_id, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return 0.20 * self.get_salary()

    def display(self):
        super().display()
        print(f"Role: Manager, Team Size: {self.team_size}")

# searching for an employee by ID


def search_employee(employees, key):
    found = False
    for emp in employees:
        if emp.employee_id == key:
            print("\nEmployee Found:")
            emp.display()
            found = True
            break
    if not found:
        print("\nEmployee Not Found")


e1 = Developer("IT", "197", 60000, "Python")
e2 = Manager("HR", "198", 80000, 5)
e3 = Developer("Finance", "199", 70000, "Java")

employees = [e1, e2, e3]

print("----- Employee Details -----")
for emp in employees:
    emp.display()
    print(f"Bonus: {emp.calculate_bonus()}\n")


print(f"Total Employees: {Employee.get_employee_count()}")


print("\n----- Search Example -----")
search_employee(employees, "197")
search_employee(employees, "103")
search_employee(employees, "199")
