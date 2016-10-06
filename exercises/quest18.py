"""Assess validity of passwords provided to the program in comma separated list
The criteria for a valid password are:
	1. At least 1 letter between [a-z]
	2. At least 1 number between [0-9]
	3. At least 1 letter between [A-Z]
	4. At least 1 character from [$#@]
	5. Minimum length of transaction password: 6
	6. Maximum length of transaction password: 12
	
Passwords that pass the validity test will be printed in a comma seprated sequence"""

print "Enter passwords to assess their validity. Spaces preceding password values will be disregarded."
passwords = [i.lstrip() for i in raw_input("Enter passwords: ").split(",")]
passed = []
booleans = {"has_low_alpha": False, "has_number": False, "has_upper_alpha": False, "has_special_char": False, "is_above_min": False, "is_within_max": False}

for s in passwords:
	if 6 <= len(s) <= 12:
		booleans["is_above_min"] = True
		booleans["is_within_max"] = True
	else:
		continue
	
	for c in s:
		if not booleans["has_low_alpha"] and c.isalpha() and c.islower(): booleans["has_low_alpha"] = True
		if not booleans["has_upper_alpha"] and c.isalpha() and c.isupper(): booleans["has_upper_alpha"] = True
		if not booleans["has_number"] and c.isdigit(): booleans["has_number"] = True
		if not booleans["has_special_char"] and c in ["$", "#", "@", "&"]: booleans["has_special_char"] = True
		
		if not False in booleans.values():
			passed.append(s)
			break
			
	for x in booleans.keys(): booleans[x] = False
	
if passed: print "Accepted passwords : %s" % ", ".join(passed)