# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 11b Program 3
# Date:        10 November, 2019

def perfectNum(num):
	# If the number is odd or less than/equal to 1 return False because it can't be perfect
	if num <= 1 and num % 2 != 0:
		return False
	else:
		smallNums = [1]
		bigNums = []
		num1 = 1
		num2 = num
		# Compute the multiple tree so long as num1 is less than num2 and not already in the lists
		while num1 <= num2 and num1 not in bigNums:
			for i in range(1,num2):
				# If the input number / num1 and the input number / i have no remainder and
				# num1*i are the input number, add it to the lists
				if num % num1 == 0 and num % i == 0 and num1*i == num:
					# If num1 == i, only append the number to one list
					if num1 == i:
						smallNums.append(i)
					# Otherwise, append it to both
					else:
						smallNums.append(num1)
						bigNums.append(i)
			num1 += 1
			num2 -= 1
		# Calculate the sum of both lists
		sumNums = sum(smallNums) + sum(bigNums)
		# If the sum of both lists together is equal to the input number, return True
		if sumNums == num:
			return True
		else:
			return False