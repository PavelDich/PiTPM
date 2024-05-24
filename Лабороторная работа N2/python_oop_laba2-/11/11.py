class Employee:
    name = "Jeb"
    surname = "Smith"
    age = 43
    salary = 2500

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        print(self.name, self.surname, self.salary)

employee = Employee("Jon", "Kotin", 1200)

