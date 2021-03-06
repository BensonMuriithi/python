from calendar import isleap

class Clock(object):
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.__hours = hours if 0<=hours<=23 else 0
		self.__minutes = minutes if 0<=minutes<=59 else 0
		self.__seconds = seconds if 0<=seconds<=59 else 0
	
	def set_time(self, hours, minutes, seconds=0):
		self.__hours = hours if 0<=hours<=23 else 0
		self.__minutes = minutes if 0<=minutes<=59 else 0
		self.__seconds = seconds if 0<=seconds<=59 else 0
	
	def tick(self):
		"""Advance time by one second"""
		if self.__seconds == 59:
			self.__seconds = 0
			if self.__minutes == 59:
				self.__minutes = 0
				self.__hours = 0 if self.__hours == 23 else self.__hours + 1
			else: self.__minutes += 1
		else: self.__seconds += 1
	
	def display(self):
		print "{0:^4}:{1:^3}:{2:^3}".format(self.__hours, self.__minutes, self.__seconds)
	
	def __str__(self):
		return "{0:^4}:{1:^3}:{2:^3}".format(self.__hours, self.__minutes, self.__seconds)


class Calendar(object):
	__days_of_month = {"January": 31, "February": 28, "March":31, "April":30, "May":31, "June":30,
				"July":31, "August":31, "September": 30, "October":31, "November":30, "December":31}
	
	__tuple_months = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
	def __init__(self, day=1, month = 1, year=1900):
		self.__month = month
		self.__year = year
		self.__day = day
	
	def display(self):
		print "{day:^3}/{month:^3}/{year:^6}".format(day = self.__day, month = self.__month, year = self.__year)
	
	def __stepup_month(self):
		if self.__month == 12:
			self.__month = 1
			self.__year += 1
		else: self.__month += 1
	
	def advance(self):
		if self.__day >= self.__days_of_month[self.__tuple_months[self.__month-1]]:
			if self.__month == 2 and isleap(self.__year):
				if self.__day == 28: self.__day += 1
				else:
					self.__day = 1
					self.__stepup_month()
				
			else:
				self.__day = 1
				self.__stepup_month()
		
		else: self.__day += 1
	
	def __str__(self):
		return "{day:^3}/{month:^3}/{year:^6}".format(day = self.__day, month = self.__month, year = self.__year)

if __name__ == "__main__":
	c = Calendar()
	c.display()
	for i in xrange(10000):
		c.advance()
	
	c.display()

