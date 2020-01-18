from math import *

# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 03b Program 2
# Date:        15 September, 2019

# Mass of Red (Held constant)
mass = 3000.0

# Prompt the user for initial and final times of the launch 
t1 = float(input("What is the starting time? "))
t2 = float(input("What is the ending time "))
diffTime = t2 - t1

# Prompt user for the initial and final coordiantes of "Red"
x1 = float(input("What is the initial x-coord? "))
y1 = float(input("What is the initial y-coord? "))
x2 = float(input("What is the final x-coord? "))
y2 = float(input("What is the final y-coord? "))

# Calculate the axis-based velocities
xVel = (x2-x1)/diffTime 
yVel = (y2-y1)/diffTime 

cVel = hypot(xVel, yVel) # Calculate the combined velocity

KE = mass*(cVel**2)/0.5 # Calculate the Kinetic Energy of Red
print(KE) # Print the final answer