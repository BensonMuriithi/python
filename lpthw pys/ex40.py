#intro to classes

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		print "I was initialised.\n"
		self.control = "Posum"
		self.pink = "\nJanelle Monae"
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def do_pink(self):
		print self.pink
		

class TestSubject(object):
	def __init__(self, num):
		self.num = num
	
	def hello(self):
		return "hello."
	
	def do_something(self):
		print "Carry On.", self.num
		print self.hello()
		
test_subject = TestSubject(1)
test_subject.do_something()


happy_birthday = Song(["Happy birthday to you", "I don't want to get sued",
						"So I'll stop right there."])
						
bulls_on_parade = Song(["They rally around the family", "with pockets full of shells"])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

happy_birthday.do_pink()