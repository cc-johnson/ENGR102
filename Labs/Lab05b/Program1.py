# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 05b Program 1
# Date:        29 September, 2019

from math import *

# Initial user input
inp = float(input("Enter your first number: ")) # User number input

# Initialize variables
sum = 0
mean = 0
count = 0
max = inp
min = inp

while inp > 0:
	sum += inp
	count += 1
	if inp > max:
		max = inp
	if inp < min:
		min = inp
	mean = (sum/count)
	inp = float(input("Enter your next number: ")) # User number input

print("\n\n------------------")
print("The mean is:", mean)
print("The max is:", max)
print("The min is:", min)
print("\nThe sum is:", sum)