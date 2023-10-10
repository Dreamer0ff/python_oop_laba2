class Employee:
    def __init__(self, name, salary, age):
        self.__name = name  
        self.__salary = salary
        self.__age = age


    def get_name(self):
        return self.__name


    def get_salary(self):
        return self.__salary


    def get_age(self):
        return self.__age


employee = Employee("Иван", 50000, 30)


print("Имя сотрудника:", employee.get_name())
print("Зарплата сотрудника:", employee.get_salary())
print("Возраст сотрудника:", employee.get_age())