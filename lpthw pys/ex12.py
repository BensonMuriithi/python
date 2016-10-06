#revision of ex11.py

name = raw_input("What's your name? ")
age = int(raw_input("How old are you? "))
height = int(raw_input("What is your height in cm? "))
weight = int(raw_input("How much do you weigh in kg? "))

print "\n\t%s\nYou're %d years old, %d cm tall and %d kg in weight." % (
	name, age, height, weight)