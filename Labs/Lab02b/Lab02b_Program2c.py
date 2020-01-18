# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson, Anna Olmedo, Bryan Jones, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 02b
# Date:        6 September, 2019

from math import *

# Time values
t1 = 20
t2 = 50
diffTime = t2 - t1 # Change in time

# Location values
x1 = 1.0
x2 = 23.0
y1 = 3.0
y2 = -5.0
z1 = 7.0
z2 = 10.0

# Determine the rate of change for each x, y, and z value pairs
mx = (x2 - x1)/diffTime
my = (y2 - y1)/diffTime
mz = (z2 - z1)/diffTime

# ------------------ .7333333333333
# t = 20.0
# ------------------

t3 = 20.0
# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("Time of interest: " + str(t3) + " seconds")
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")
print("------------------")

# ------------------
# t = 27.5
# ------------------

t3 = 27.5
# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("Time of interest: " + str(t3) + " seconds")
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")
print("------------------")

# ------------------
# t = 35.0
# ------------------

t3 = 35.0
# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("Time of interest: " + str(t3) + " seconds")
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")
print("------------------")

# ------------------
# t = 42.5
# ------------------

t3 = 42.5
# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("Time of interest: " + str(t3) + " seconds")
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")
print("------------------")

# ------------------
# t = 50.0
# ------------------

t3 = 50.0
# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("Time of interest: " + str(t3) + " seconds")
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")
print("------------------")
