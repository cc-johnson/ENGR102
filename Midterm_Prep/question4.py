"""
The Maclaurin series expansion for 1/(1-x) on an interval from -1 < x < 1 is as follows:

Write Python code which asks for input of a value of x on the interval -1 < x < 1, 
and which computes an approximation to 1/(1-x) using the using the series expansion
summation. The summation should be continued until the term to be added to the
summation is less than 10^-6 in absolute value. Hint: Note that each term in the
series is x raised to a power, including the 1 and x terms: x^0=1 and x^1=x
"""
from math import fabs 

x = float(input("Give me an x value so that -1 < x < 1: "))

sum = 0
n = 0
while (fabs(x ** n)) > (10 ** (-6)):
	sum += x ** n
	n += 1

print("The Maclaurin series expansion for 1/(1-x) where x = " + str(x) + " is: " + str(sum))
