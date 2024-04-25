class User:
	def __init__(self, name, surname) -> None:
		self.name = name
		self.surname = surname
	    
	def get_name(self):
		return self.name
	
	def get_surname(self):
		return self.surname

class Employee(User):
	def __init__(self, name, surname, age, salary):
		super().__init__(name, surname)
		self.age = age
		self.salary = salary
	
	def get_age(self):
		return self.age
	
	def grt_salary(self):
	    return self.salary