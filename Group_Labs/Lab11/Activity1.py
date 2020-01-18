# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 11 Activity 1
# Date:        10 November, 2019

# stats(nums) is a function that takes in one argument: $nums
# assuming $nums is a list
def stats(nums):
	# Get the minimum of $nums
	minimum = min(nums)
	# Get the maximum of $nums
	maximum = max(nums)
	# Determine the mean of $nums
	listMean = sum(nums)/len(nums)
	# Return calculated values as tuple in order of calculation
	return (minimum, maximum, listMean)

print(stats(nums))
a = stats(nums)
