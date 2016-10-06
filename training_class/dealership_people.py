from car_dealership import Dealership

class Customer(object):
	dealership = Dealership
	
	def __init__(self, name, vehicle=None):
		self.name = name
		self.vehicles = set()
	
	def buy_vehicle(self, vehicle, sales_person):
		self.vehicles.add(vehicle)
		self.dealership.sell(vehicle, self, sales_person)
	
	def sell_vehicle(self, vehicle, presiding_officer):
		self.vehicles.add(vehicle)
		self.dealership.buy(vehicle, self, presiding_officer)


class SalesPerson(object):
	dealership = Dealership
	
	cars_sold = set()
	
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
	
	def sell_vehicle(self, vehicle, customer):
		cars_sold.add((vehicle, customer))
	