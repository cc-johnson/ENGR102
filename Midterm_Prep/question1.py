"""
Write a Python program that takes as inputs 5 integers. The program should check to see if any of the 5 are
duplicates of another (i.e., check whether any of the integers were entered more than once). If, after all
inputs are entered, a duplicate is found, the program should print “Duplicates”, otherwise it should print
“All Unique”.
"""

dups = False

nums = []

for i in range(5): # Loop 5 times
	num = float(input("Give me number " + str(i+1) + ": ")) # Ask user for number input $num

	if num in nums: # Check to see if the number is already in $nums
		dups = True # If the number already exists in $nums, set $dups to True
		nums.append(num) # Still want to append it so we have the number
	else:
		nums.append(num) # Otherwise, append $num to the list $nums

if dups == True: # If $dups is True
	print("Duplicates") # Print "Duplicates"
else: # else (basically saying if $dups is False)
	print("All unique") # Print "All unique"