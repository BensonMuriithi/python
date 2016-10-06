class InvalidEmailError(ValueError): pass
class NegativeAgeError(ValueError): pass
class DuplicateUserNameError(ValueError): pass
class UnderAgeError(ValueError): pass

def loop_data(*args):
	users = {}
	for user in args:
		try:
			if user[0] in users: raise DuplicateUserNameError("The username {} already exists in the database".format(user[0]))
			if user[2] < 0: raise NegativeAgeError("The age {} is invalid".format(user[2]))
			if user[2] < 16: raise UnderAgeError("a user of this service must be at least 16 old.")
			if not user[1].count("@") is 1: raise InvalidEmailError("The email entered must be a valid email address")

			users[user[0]] = user[1]
		except ValueError:
			pass