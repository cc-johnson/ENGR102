"""
Given a list xdata of unknown length that contains x values, write the code
to calculate a y-value for each x-value using the equation below. Store the
calculated y values in a list called y_data. Do not use numpy arrays for this
problem. Please use Python list functions, list methods, and list operators.
y = 4.12x^2 + 1.52x - 7.1
"""

# Ignore this section, I'm just generating a list of random values
from random import random, uniform
xData = [uniform(-i,i) for i in range(20)] # This just generates 20 random floats
# Ok stop ignoring me

y_data = [] # list of f(x) or y values
for x in xData: # for every $x value in $xData
	funcX = 4.12*(x**2) + 1.52*(x) - 7.1 # Calculate the f(x) value for the current $x
	y_data.append(funcX) # append the $funcX value to $y_data

# Print out the two lists
print(xData)
print(y_data)