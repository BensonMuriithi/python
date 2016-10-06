#practice

print "Let's practise."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "-" * 14
print poem
print "-" * 14

fie = 10 - 2 + 3 - 6
print "This should be five \'how do you know?': %s" % fie

def secret_Formula(started):
	jellys = started * 500
	jars = jellys / 1000
	crates = jars / 100
	return jellys, jars, crates
	
start_point = 10000
beans, jars, crates = secret_Formula(start_point)

print "With a start point of %d: "% start_point
print "We'd have %d jelly beans, %d jars of, and %d crates of." % (beans, jars, crates)

start_point /= 10

print "We could also have it this way: "
print "We'd have %d jelly beans, %d jars of, and %d crates of." % secret_Formula(start_point)