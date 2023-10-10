class Employee:
    name = "Vladimir"
    age = 69
    salary = 2000
    def print_properties(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


info = Employee()
info.print_properties()