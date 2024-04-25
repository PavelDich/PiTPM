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

    def add(self, emp):
        self.__emps.append(emp)

    def show(self):
        for emp in self.__emps:
            print(emp.getName())

    def sum_sal(self):
        summ_sal = 0
        for emp in self.__emps:
            summ_sal += emp.salary