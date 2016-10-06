#a bit complex printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are some months: ",months

print """
There's something going on here.
With three double-quotes
We can print as much as we like.
We can print as many lines as we like: %d, %d, %d, %d..
"%s"
Remember to end this set of strings with a triple double-quote.
""" % (3,4,5,6, 'Can I do this?')