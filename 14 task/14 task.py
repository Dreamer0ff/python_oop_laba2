class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def getSalary(self):
    return self._addSign(self.salary)

  def _addSign(self, num):
    return num + '$'