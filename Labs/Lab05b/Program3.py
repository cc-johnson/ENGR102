# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 05b Program 3
# Date:        29 September, 2019

from math import tan, cos, pi
import numpy
import matplotlib.pyplot as plt

inVel = float(input("What is Red's initial velocity? "))
deltTheta = float(input("At what rate do you want to change the angle of launch? "))

theta = 0 # Angle of launch
x = 202.3 # Distance Red need's to get shot
y = (x*tan(theta))-(((9.807)*(x**2))/(2*(inVel**2)*(cos(theta)**2))) # Formula for initial distance Red will travel
max = y
xvals = 0
yvals = 0

while y < x and y >= max:
	theta += (deltTheta) * pi / 180
	y = (x*tan(theta))-(((9.807)*(x**2))/(2*(inVel**2)*(cos(theta)**2)))
	if y > max:
		max = y

if y > x:
	print("\nThe angle to launch on Earth with an initial velocity of", inVel, "is:", theta)
	# --------------------------
	# Begin matplotlib and numpy
	# --------------------------
	# Create x-values for plot
	xvals = numpy.arange(0, max, 0.01) # Values with 0.01 spacing from bounds a to b

	# Create y-values for plot (from function)
	yvals = (xvals*tan(theta))-(((9.807)*(xvals**2))/(2*(inVel**2)*(cos(theta)**2))) # Evaluate function at every point defined by xvals. What function is shown here?
else:
	print("Red must start at a different velocity to succeed on Mars")

print("The above calculation is for on Earth, let's try with Mars:")

# All Mars variables are identical to those used for Earth but have a 'm'
# in front of the name
mtheta = 0 # Angle of launch
my = (x*tan(mtheta))-(((3.711)*(x**2))/(2*(inVel**2)*(cos(mtheta)**2))) # Formula for initial distance Red will travel
mmax = my
mxvals = 0
myvals = 0

while my < x and my >= mmax:
	mtheta += (deltTheta) * pi / 180
	my = (x*tan(mtheta))-(((3.711)*(x**2))/(2*(inVel**2)*(cos(mtheta)**2)))
	if my > mmax:
		mmax = my

if my > x:
	print("\nThe angle to launch on Earth with an initial velocity of", inVel, "is:", mtheta)
	# --------------------------
	# Begin matplotlib and numpy
	# --------------------------
	# Create x-values for plot
	mxvals = numpy.arange(0, mmax, 0.01) # Values with 0.01 spacing from bounds a to b

	# Create y-values for plot (from function)
	myvals = (mxvals*tan(mtheta))-(((3.711)*(mxvals**2))/(2*(inVel**2)*(cos(mtheta)**2))) # Evaluate function at every point defined by xvals. What function is shown here?
else:
	print("Red must start at a different velocity to succeed on Mars")

# Create and show plot
plt.plot(xvals, yvals, "g--", mxvals, myvals, "r--") # Create line plot with yvals against xvals
plt.show() # Show the figure

print("\n\nThe final distance traveled on Earth is:", y, "and on Mars is:", my)