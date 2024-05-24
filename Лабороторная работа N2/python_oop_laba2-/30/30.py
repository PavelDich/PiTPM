class Employee:
    __name = "Jon"
    __age = 20
    __salary = 100

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSalary(self):
        return str(self.__salary) + "$"

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSalary(self, salary):
        self.__salary = salary


employee = Employee("Skibidi", 10, 0)
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())
employee.setName("Bran")
employee.setAge(66)
employee.setSalary(121)
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())
