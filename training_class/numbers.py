class Numbers:
	MULTIPLIER = 42
	def __init__(self, x, y):
		self.x = x; self.y = y
	
	def add(self):
		return self.x + self.y
	
	@classmethod
	def multiply(cls, a):
		return a * cls.MULTIPLIER
	
	@staticmethod
	def subtract(b, c):
		return b - c
	
	def value(self):
		return self.x, self.y