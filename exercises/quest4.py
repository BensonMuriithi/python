"""Acquire input from the console which contains comma separated numbers. Pick out the numbers from the input and
place the numbers in a list and a tuple and finally print both structures."""

string = raw_input("Enter numbers separated by commas : ")
no_comms = string.split(',')

num_list = []
for x in no_comms:
	num_list.append(int(x))

print num_list
print tuple(num_list)