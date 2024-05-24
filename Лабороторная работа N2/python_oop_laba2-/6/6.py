class Employee:
    name = "Jeb"
    age = 43
    salary = 2500

    def info(self, name, salary):
        Employee.name = name
        Employee.salary = salary
        print(Employee.name, Employee.age, Employee.salary)

employee = Employee()
employee.info("Brown", 3100)