class Employee:
    __name = "Jon"
    __age = 20
    __salary = 100

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        print(self.__name)

    def getAge(self):
        print(self.__age)

    def getSalary(self):
        print(self.__salary)

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSalary(self, salary):
        self.__salary = salary


employee = Employee("Skibidi", 10, 0)
employee.getName()
employee.getAge()
employee.getSalary()
employee.setName("Bran")
employee.setAge(23)
employee.setSalary(102)
employee.getName()
employee.getAge()
employee.getSalary()

