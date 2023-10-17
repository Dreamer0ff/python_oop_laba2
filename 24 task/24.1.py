class Employee():
    name = None
    salary = None
    age = None
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

workers = [Employee("Walt", 80000, 19), Employee("Jesse", 87000, 18), Employee("Mike", 1123000, 25)] # 24.1

for worker in workers: # 24.2
    print(worker.name, worker.salary)