"""Provide information on all for access functions of an object"""

from re import findall as re_findall

def info(thing):
	"""Prints the callables of a supplied argument: module, class, list, dict etc
	and their documentations
	"""
	
	access_methods = [m for m in dir(thing) if callable(getattr(thing, m)) and not m.startswith("__")]
	process_doc = lambda f: "\n".join(["{:>10}{}".format("", s) for s in re_findall(r".{,90}\w*", f.__doc__)]) if f.__doc__ else "None"
	
	print
	if callable(thing): print "{:>4}{}(..)\n{}".format("", thing.__name__, process_doc(thing))
	
	if access_methods:
		print "\n".join(["{justify:>4}{the_method}(..)\n{the_docs}".format(justify = "", the_method = method,
				the_docs = process_doc(getattr(thing, method))) for method in access_methods])
	
if __name__ == "__main__":
	print info.__doc__

