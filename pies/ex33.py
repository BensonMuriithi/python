#while loops

def make_list(upper):
	i = 0
	nums = []
	while i < upper:
		nums.append(i)
		i += 1
		print "Numbers now: ", nums
		
	print "The numbers: ",
	for n in nums:
		print n,
		
make_list(15)