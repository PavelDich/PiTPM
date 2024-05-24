class Student:
    name = "Jeb"
    surname = "Smith"

    def initials(self):
        return self.cape(self.name)

    def capitalized(self, stri):
        if self.name[0] == stri:
            return self.name[0].upper() + self.name[1:len(self.name)]


student = Student()
student.name = "george"
print(student.capitalized("g"))
