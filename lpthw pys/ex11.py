#introduction to input

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh in kilograms?",
weight = raw_input()

print """
So you're %r years old, %r cm tall and %rkg in weight
""" % (age, height, weight)