# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 11b Program 2
# Date:        10 November, 2019

def printAddress(name, city, state, zip, addr1, addr2=''):
	# Print name
	print(name)
	# If addr2 is not blank, print it after addr1
	if addr2.strip() != '':
		# Print addr1 and addr2
		print(addr1)
		print(addr2)
	else:
		# Print addr1
		print(addr1)
	# Print the remaining parts of the address on one line
	print(city + ', ' + state + ' ' + str(zip) + '\n')