from datetime import date

class Person(object):
	def __init__(self, name, surname, birthdate, address, telephone, email):
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.address = address
		self.telephone = telephone
		self.email = email
		self.__age_calculation = ""
		self._age = self.age()
	
	def age(self):
		current_date = date.today()
		if self.__age_calculation == str(current_date):
			return self._age
		
		self.__age_calculation = str(current_date)
		self._age = current_date.year - self.birthdate.year
		
		if current_date < self.birthdate.replace(year=current_date.year):#this year's birthday hassn't yet arrived
			self._age-= 1
		
		return self._age
	
	def __str__(self):
		return "{name}, {age}: Address - {address} Telephone - {phone} Email - {email}".format(name = self.name+" "+self.surname,
			age=self.age, address=self.address, phone = self.telephone, email=self.email)
	
	def __eq__(self, other):
		return (self.name == other.name and self.surname == other.surname)
	
	def __gt__(self, other):
		return self.name > other.name if self.surname==other.surname else self.surname > other.surname
	
	def __lt__(self, other):
		return not (self > other or self == other)
	
	def __ge__(self, other):
		return not self < other
	
	def __le__(self, other):
		return not self > other

p = Person(
	"Ann",
	"Winner",
	date(1995, 4, 30),
	"751 Thika, Kenya",
	"+254 716 321 415",
	"annwinner95@tts.com"
)

print p.name
print p.age()

print
print dir(p)
print
print dir(Person)