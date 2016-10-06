#practice lists

things = "Apples Oranges Crows Telephone Sugar Light"
print "Wait, there's not 10 things in that list. Let's fix that"

stuff = things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next = more_stuff.pop()
	print "Adding %s to stuff." % next
	stuff.append(next)
	print "There's now %d items in list stuff." % len(stuff)
	
print "That solves that."
print "Let's now play with the list stuff."

print stuff[1]#oranges
print stuff[-1]#corn#-1 gets last element in list
print stuff.pop()#Banana and now list has 9 items.
print ' '.join(stuff)#turn items in list into a string with the provided separator btwn every element in string

#elements of stuff from indec 3 to 4
#index 5 is the upper limit and is excluded from the returned list
print '#'.join(stuff[3:5])#quite fancy. let's see its purpose.