class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def increase_salary(self):
        self.salary *= 1.10

# Пример использования класса:
employee1 = Employee("Иван Иванов", 50000)
print("Имя работника:", employee1.get_name())
print("Зарплата работника:", employee1.get_salary())

employee1.increase_salary()
print("Новая зарплата после увеличения на 10%:", employee1.get_salary())