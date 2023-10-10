class Employee:
    name = "Vladimir"
    salary = 200000
    def print_properties(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


info = Employee()
info.print_properties()