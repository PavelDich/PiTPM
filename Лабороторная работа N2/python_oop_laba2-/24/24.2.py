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


empls = [
    Employee('Eric', 'Industries Co.', 'Manager', '3500'),
    Employee('Arthur', 'Industries Co.', 'CEO', '9000'),
    Employee('Edward', 'Industries Co.', 'Junior', '3000')
]

for empl in empls:
    print(empl.name, empl.salary)