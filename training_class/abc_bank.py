"""Class to represent a customer of a certain bank.
The bank will be ABC bank."""


class Customer(object):
	"""
	Attributes of customer will be:
		name -> name of customer
		balance -> float value of balance customer as in bank
	
	Methods'll be:
		withdraw -> facilitate withdrawal of finances from customer's account
		deposit -> facilitate deposit of finances to account
	"""
	
	def __init__(self, name, balance=0.0):
		self.name = name
		self.balance = balance
	
	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError("Amount requested for withdrawal exceeds balance in customer's account.")
		
		self.balance -= amount
		return amount
	
	def deposit(self, amount):
		if amount < 0.0:
			raise RuntimeError("Amount to deposit is below the permitted minimum.")
		
		self.balance += amount
		return self.balance
	
	def fetch_balance(self):
		return self.balance
	
	@staticmethod
	def fetch_bank():
		return "ABC Bank"

