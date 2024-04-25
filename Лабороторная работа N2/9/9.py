class Student:
    name = "Jeb"
    surname = "Smith"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

student = Student("Katrin", "Johans")
print(student.name, student.surname)
