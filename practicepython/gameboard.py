"""Draw a X x Y matrix as per the specifications entered as input"""

def draw(x, y):
	"""Draws a matrix of x rows and y columns"""
	
	##The length of the 'dott' sequence can be adjusted and the rest of the
		#drawing will adjust itself after reloading"""
	dott = "  -----  "
	pipe = "|"
	
	print "\n"
	if y: print dott * x + "\n"
	for i in xrange(y):
		#Though not very readable, the line below is responsible for determining how long
			#one y(vertical) cell should be and printinng as many pipes along the y axis
			 #after considering the width of a cell(x-axis unit) 
		#The initial part before the final times sign prints 1 + the number of 
			#cells along the x axis (rows) inorder to close last cell   
			#the calculation of the spacing of the pipes was determined after testing
				#for the best fit
		
		print ((" "*(len(dott)-1)).join(iter(pipe*(x+1))) + "\n") * (len(dott) / 2)
		
		print dott*x + "\n"
		
if __name__ == "__main__":
	x = y = None
	while x == None or y == None:
		try:
			x, y = raw_input("\nEnter a matrix to draw eg(3x3) >> ").lower().split("x")
		except ValueError: pass
	draw(int(x), int(y))

