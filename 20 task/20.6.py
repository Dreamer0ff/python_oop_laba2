class Employee:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name
        return False

emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 != emp2)