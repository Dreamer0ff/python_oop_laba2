class Employee:
    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary



employee1 = Employee()
employee2 = Employee()
employee3 = Employee()


employee1.set_name("Иван")
employee1.set_salary(50000)

employee2.set_name("Мария")
employee2.set_salary(55000)

employee3.set_name("Алексей")
employee3.set_salary(48000)


total_salary = employee1.salary + employee2.salary + employee3.salary


print("Сумма зарплат созданных работников: ", total_salary)
