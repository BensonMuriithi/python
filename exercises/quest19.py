"""Sort a set of (name, age height) tuples in ascending order and return them"""

collect = []

while True:
	ss = [i.lstrip() for i in raw_input('Enter person\'s details: ').split(",")]
	if len(ss) < 2: break
	if len(ss) == 2: ss.append("0")
	collect.append(tuple(ss[0:3]))
	
print sorted(collect)