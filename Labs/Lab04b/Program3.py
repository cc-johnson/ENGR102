# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 04b Program 3
# Date:        22 September, 2019

import math as m

print("------------------")
print("This program identifies the x intercepts of a quadratic equation\nin the form Ax^2 + Bx + C = 0\n")

# Get inputs
a = float(input("What is your A value? "))
b = float(input("What is your B value? "))
c = float(input("What is your C value? "))

# Quadratic equation terms
term1 = -1 * b
term2 = (b**2) - (4 * a * c)
den = 2 * a

# Determine if imaginary
if term2 < 0:
	i = True
	term2 = abs(term2)
else:
	i = False

# Evaluate the sqrt part
term2 = m.sqrt(term2)

# Divide both terms by the denominator
term1 = term1 / den
term2 = term2 / den

# Determine if term2 is negative and insert the proper string operator
if term2 < 0:
	pm = "-"
	nm = "+"
else:
	pm = "+"
	nm = "-"

if i == True:
	term2 = abs(term2)
	posNum = str(term1) + " " + pm + " " + str(term2) + "i"
	negNum = str(term1) + " " + nm + " " + str(term2) + "i"
else:
	term1 = term1 + term2
	posNum = str(term1)
	negNum = str(term1)

print("\n\n------------------")
print("X roots: " + "(" + str(posNum) + "), (" + str(negNum) + ")")