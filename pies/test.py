class Person(object):
	numof_people = 0
	def __init__(self, name):
		self.name = name
		Person.numof_people += 1
		
	def __del__(self):
		print "You're deleting a person..!!!weep!\n"
		
class Employee(Person):
	"Documentation for the employee class definition"
	
	__pension_code = 5781013
	
	number_of_employees = 0
	def __init__(self, name=None, pay=0):
		self.salary = pay
		super(Employee, self).__init__(name)
		Employee.number_of_employees += 1
	
	def sing(self, lyrics):
		print lyrics
	
	def pension(self):
		self.__secretMethod()
	
	def __secretMethod(self):
		print Employee.__pension_code
	def __del__(self):
		super(Employee, self).__del__()

Employee.company = "Benson Muriithi studios\n"
Kaylie = Employee("Ann", 500000)
Kaylie.sing("Let's do it again")
print Kaylie.company

if isinstance(Kaylie, Person):print "Is instance"
if issubclass(Kaylie.__class__, Person):print "Is subclass\n"

Kaylie.pension()
del Kaylie