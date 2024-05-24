class User:
    _name = None
    _age = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

class Employee(User):
    salary = None

    def setAge(self, salary):
        self._salary = salary

class Programmer(Employee):
    _speed = None

    def printParameter(self):
        print(self._speed, self.salary)

class Designer(Employee):
    _creativity = None

    def printParameter(self):
        print(self._creativity, self.salary)