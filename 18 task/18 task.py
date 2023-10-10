class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age  # Здесь используется _age для представления возраста согласно PEP 8
        self._salary = salary  # Здесь используется _salary для представления зарплаты согласно PEP 8

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError("Возраст должен быть от 0 до 120")

    @property
    def salary(self):
        return f"${self._salary}"

    @salary.setter
    def salary(self, value):
        self._salary = value

# Пример использования класса Employee:
employee = Employee("Иван", 30, 50000)
print(f"{employee.name}, возраст: {employee.age}, зарплата: {employee.salary}")
employee.age = 25  # Установка нового возраста
employee.salary = 60000  # Установка новой зарплаты
print(f"Новый возраст: {employee.age}, Новая зарплата: {employee.salary}")