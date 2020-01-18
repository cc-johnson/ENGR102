# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 5
# Date:        13 October, 2019

from math import fabs

sum = 1.0
# Take input for x value
x = float(input("Give me an x so that -1 < x < 1: "))

n = 1
# Adds each new calculation to the sum to compute the final answer
while fabs(x ** n) > (10 ** -6):
	sum += x ** n
	n += 1
	# print("n = %4d | sum = %.9f " % (n, sum))

# Print the sum
print()
print(round(sum,2))