"""Identify the odd numbers in a list entered as input and print them"""

print "Identify odd numbers\n"
odds = [i.lstrip() for i in raw_input("Enter list of numbers: ").split(",") if int(i) % 2 != 0]

print ", ".join(odds)