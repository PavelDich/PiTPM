class Employee:
    name = "Jeb"
    age = 43
    salary = 2500

    def info(self):
        print(Employee.name, Employee.age, Employee.salary)

employee = Employee()
employee.info()
