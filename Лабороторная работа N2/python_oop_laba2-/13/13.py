class Employee:
    __name = "Jeb"
    surname = "Smith"
    __age = 43
    __salary = 2500

    def __init__(self, name, surname, salary):
        self.__name = name
        self.surname = surname
        self.__salary = salary

    def Show(self):
        print(self.__name, self.surname, self.__age, self.__salary)

employee = Employee("Jon", "Kotin", 1200)
employee.Show()

