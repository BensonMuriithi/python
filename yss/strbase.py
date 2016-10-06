from string import uppercase

dig_to_chr = lambda num: str(num) if num < 10 else uppercase[num - 10]

def strbase(number, base):
	if not 2 <= base <= 36:
		raise ValueError("Base to convert to must be >= 2 and <= 36")
	
	if number < 0:
		return "-" + strbase(-number, base)
	
	d, m = divmod(number, base)
	if d:
		return strbase(d, base) + dig_to_chr(m)
	
	return dig_to_chr(m)
