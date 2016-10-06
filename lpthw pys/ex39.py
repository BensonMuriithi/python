#dictionaries

#dict states and their abbreviations
states = {"Oregon": "OR", "Florida" : "FL", "California" : "CA", 
	"New York" : "NY", "Michigan" : "MI"}
	
cities = {"CA" : "San Fransisco", "MI" : "Detroit", "FL" : "Jacksonville"}

#add cities to the cities dict
cities["NY"] = "New York"; cities["OR"] = "Portland"

print '_' * 10
print "NY state has:", cities["NY"]
print "OR state has:", cities["OR"]

print '_' * 10
print "Michigan's abbreviation is:", states["Michigan"]
print "Florida's abbreviation is:", states["Florida"]

print '_' * 10
print "Michigan has:", cities[states["Michigan"]]
print "Florida has:", cities[states["Florida"]]

#print out all abbreviations
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)
	
#print every city in state
print '_' * 10
for abb, city in cities.items():
	print "%s has the city %s" % (abb, city)
	
#print state abbrev and city
print '_' * 10
for state, abb in states.items():
	print "%s is abbreviated as %s and has the wonderful city %s" % (state, abb, cities[abb])
	
#safely get the abbreviation of a state that might not be in dictionary
state = states.get("Texas", None)
if not state:
	print "Sorry, no Texas."
	
#get a city with a default return values
city = cities.get("TX", "Does not exist")
print "The city for the state TX is:", city