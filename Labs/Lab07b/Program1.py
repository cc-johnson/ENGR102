# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 07b Program 1
# Date:        13, October 2019

array = [[1,2],
		 [13,4],
		 [11,6],
		 [7,8]] # Define the 2D list to be used, assuming there should be no user input

highTerm = [] # The term with the highest sum
sumHigh = 0 # The sum of the numbers in the highest term
for row in array: # Iterating the 2D list
	sumTerms = sum(row) # Calculate the sum of the current term
	if sumTerms > sumHigh: # If that sum is greater than the current sum, make it the new max
		highTerm = [row] # Highest term is now this term
		sumHigh = sumTerms # The sum of the highest term is now this
	elif sumTerms == sumHigh: # Also, if the sum of the terms is equal to the current max, add that term to the highTerms list
		highTerm.append(row) # Add the term to the highTerm list

# Print the result
print("2D List:", array) 
print("The highest term is:", highTerm, "with a value of:", sumHigh)