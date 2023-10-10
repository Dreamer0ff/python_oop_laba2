class Employee:
    def __init__(self):
        self.name = "Vladimir"
        self.salary = 200000
    def print_name(self):
        print("Name:", self.name)
    def print_salary(self):
        print("Salary:", self.salary)


info = Employee()
info.print_name()
info.print_salary()