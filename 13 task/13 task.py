class Employee:
    def __init__(self, name, salary, age):
        self.__name = name  # Приватное свойство имени
        self.__salary = salary  # Приватное свойство зарплаты
        self.__age = age  # Приватное свойство возраста

    def display_employee_info(self):
        print(f"Имя: {self.__name}")
        print(f"Зарплата: {self.__salary}")
        print(f"Возраст: {self.__age}")

# Создаем объект класса Employee
employee1 = Employee("Иван", 50000, 30)

# Выводим данные о работнике
employee1.display_employee_info()