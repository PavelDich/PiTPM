class Employee:
    name = None
    company = None
    status = None
    salary = None

    def __init__(self, name, company, status, salary):
        self.name = name
        self.company = company
        self.status = status
        self.salary = salary


class EmployeeCollection:
    __emps = None

    def __init__(self):
        self.__emps = []
