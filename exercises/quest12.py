"""find all numbers between 1000 and 3000 of hich every digit in the number is an even number"""

results = []

for i in range(1000, 3000 + 1):
	s = str(i)
	for j in range(0, len(s)):
		if int(s[j]) % 2 != 0:
			break
		elif j == len(s) - 1:
			results.append(s)
			
print " ".join(results)