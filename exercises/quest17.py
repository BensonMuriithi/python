"""Calculate the net amount in a bank account based on transaction representations presented as input
'D' represents deposit and 'W' represents withdrawal
eg D 500
   W 200
   ->the net amount is 300
"""

class TransactionTypeError(Exception):
	def __init__(self, msg):
		self.message = msg
	def __str__(self):
		return self.message
		

net = 0

print "Enter transactions for net amount."
while True:
	sp = raw_input("Enter transaction : ").split()
	if len(sp) < 2: break
	if sp[0].upper() == "D": net += int(sp[1])
	elif sp[0].upper() == "W": net -= int(sp[1])
	else:
		message = "Transaction entered: %s is invalid" % sp[0]
		raise TransactionTypeError(message)
	
print "Net amount %d" % net