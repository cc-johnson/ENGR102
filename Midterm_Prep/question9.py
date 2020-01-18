"""
Write a Python program which uses loops that can output the following pattern.
1
22
333
4444
55555
666666
7777777
88888888
"""

for i in range(8): # Loop 8 times with an incremented number each time
	for j in range(i+1): # Loop $i+1 times
		print(str(i+1),end="") # Print out $i+1, $i times (i.e. print 6, 6 times)
	print() # Make a new line
