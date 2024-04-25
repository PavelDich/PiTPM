class Employee:
    name = "Jeb"
    salary = 2500

    def info(self):
        print(self.name, self.salary)

employee = Employee()
employee.name = "Brown"
employee.age = 3100
employee.info()