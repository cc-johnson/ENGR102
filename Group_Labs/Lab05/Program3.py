# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Chase Johnson, Bryan Jones, Anna Olmedo
# Section:     413
# Assignment:  Lab Assignment 5, Activity 3
# Date:        23 September 2019

# Coefficient values for cubic function Ax^3 + Bx^2 + Cx + D; a must be less than b
a = float(input('Input value of a: '))
b = float(input('Input value of b: '))
c = float(input('Input value of c: '))
d = float(input('Input value of d: '))

# Upper and lower bounds and midpoint 'p'
max = float(input('Input the upper bound value: '))
min = float(input('Input the lower bound value: '))
if min > max:
    tmp = max
    max = min
    min = tmp
iMax = max # For use with matplotlib
iMin = min # For use with matplotlib
p = ((max - min) / 2) + min

# Evaluate cubic function
fP = (a * (p ** 3)) + (b * (p ** 2)) + (c * p) + d

# Bisection
while fP != 0:
    fP = (a * (p ** 3)) + (b * (p ** 2)) + (c * p) + d               # Function of p (midpoint)
    fMin = (a * (min ** 3)) + (b * (min ** 2)) + (c * min) + d       # Function of min
    fMax = (a * (max ** 3)) + (b * (max ** 2)) + (c * max) + d       # Function of max
    if ((fMin < 0) and (fP > 0)) or ((fMin > 0) and (fP < 0)):
        max = p
    elif ((fMax > 0) and (fP < 0)) or ((fMax < 0) and (fP > 0)):
        min = p
    p = ((max - min) / 2) + min

print('Finished', p)

# --------------------------
# Begin matplotlib and numpy
# --------------------------
import numpy
import matplotlib.pyplot as plt

# Create x-values for plot
xvals = numpy.arange(iMin, iMax, 0.01) # Values with 0.01 spacing from bounds a to b

# Create y-values for plot (from function)
yvals = (a * (xvals ** 3)) + (b * (xvals ** 2)) + (c * xvals) + d # Evaluate function at every point defined by xvals. What function is shown here?

# Create and show plot
plt.plot(xvals, yvals) # Create line plot with yvals against xvals
plt.show() # Show the figure