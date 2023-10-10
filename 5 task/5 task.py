class Employee:
    name = "Vladimir"
    age = 69
    def print_properties(self):
        print("Name:", self.name)
        print("Age:", self.age)


info = Employee()
info.print_properties()