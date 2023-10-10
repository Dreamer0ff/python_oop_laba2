class Employee:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name
        return False

emp1 = Employee('john')
emp2 = emp1
emp2.name = 'eric'

print(emp1 == emp2)