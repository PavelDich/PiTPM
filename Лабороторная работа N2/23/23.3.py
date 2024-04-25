class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


class Employee:
    company = None
    status = None

    def __init__(self, company, status):
        self.department = company
        self.position = status

empl = Employee('Industries Co.', 'manager')
arthur = User('Arthur', empl.position, empl.department)

print(arthur.name, arthur.department, arthur.position)