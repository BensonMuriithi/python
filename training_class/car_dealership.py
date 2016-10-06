from abc import ABCMeta, abstractmethod
from time import time

class Dealership(object):
	__metaclass__ = ABCMeta
	
	@staticmethod
	def sell(vehicle, customer, sales_person):
		vehicle.sell_vehicle(customer, sales_person)
		sales_person.sell_vehicle(vehicle, customer)
	
	@staticmethod
	def buy(vehicle, source, officer):
		vehicle.buy_vehicle(source, officer)
	
	@abstractmethod
	def sup(self): pass

	
class Vehicle(object):
	"""Abstract base class for vehicles represented in the dealership
	
	Attributes:
		wheels -> integer pf number of wheels on the vehicle
		miles -> float of the number of miles covered by the vehicle
		make - > string of make of vehicle
		model -> string of name of vehicles model
		year -> integer holding year the vehicle was released
		sold_on ->the date the vehicle was sold from the dealership
	"""
	
	__metaclass__ = ABCMeta
	
	buying_types = {"Car": 8000.00, "Truck": 10000.00, "Motorcycle": 4000.00}
	
	def __init__(self, wheels, miles, make, model, year, sold_on):
		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
		self.buying_info = {"Presiding Officer": "", "Source": ""}
		self.sales_person = None
		self.customer = None
	
	def selling_price(self):
		if self.sold_on:
			return 0.00
		
		return self.wheels * 5000.00
	
	def purchasing_price(self):
		if not self.sold_on:
			return 0.00
		
		return Vehicle.buying_types[self.vehicle_type()] - (.10 * self.miles)
	
	def sell_vehicle(self, customer, sales_person):
		self.sold_on = str(time())
		self.sales_person = sales_person
		self.customer = customer
	
	def buy_vehicle(self, source, buying_person):
		self.buying_info["Presiding Officer"] = buying_person
		self.buying_info["Source"] = source
	
	@abstractmethod
	def vehicle_type(self):
		"""Return a string holding the type of vehicle one is"""
		pass


class Car(Vehicle):
	"""Class representing Cars in the dealership"""
	
	def vehicle_type(self):
		return "Car"

class Truck(Vehicle):
	"""Class representing Trucks in Beams tech dealership"""
	
	def vehicle_type(self):
		return "Truck"

class Motorcycle(Vehicle):
	"""Class representing Motorcycles in Beams tech dealership"""
	
	def vehicle_type(self):
		return "Motorcycle"

