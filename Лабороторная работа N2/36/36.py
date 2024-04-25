class User:
	__name = None

	def setName(self,name):
		self.__name = name

	def getName(self):
		return self.__name

class Employee(User):
	def setName(self, name):
		if len(name) > 0:
			self.setName(name)

user = Employee
user.setName("Piter")