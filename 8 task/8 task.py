class Student:
    name = "Vladimir"
    surname = "Putin"

    def show(self):
        return self.cape(self.name + ' ' + self.surname)

    def cape(self, str):
        return str.title()

    def initials(self):
        return  self.name[0].title() + ". " + self.surname[0].title() + '.'


student = Student()
print(student.show())
print(student.initials())
