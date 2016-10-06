"""Accept string from im=nput and calculate the occurence of every word in the input
print the results in alphanumeric order for the words"""

entered = raw_input("Enter sentence: ").split()

results = {}

for i in range(0, len(entered)):
	if results.has_key(entered[i]): results[entered[i]] += 1
	else: results[entered[i]] = 1
	
for x in sorted(results.keys()):
	print "%s: %d" % (x, results[x])