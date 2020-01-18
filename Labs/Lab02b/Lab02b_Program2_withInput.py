# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab ##
# Date:        15 September, 2019

from math import *

# Time values
t1 = float(input("What is your initial time? "))
t2 = float(input("What is the final time? "))
t3 = float(input("What is the time of interest? "))
diffTime = t2 - t1 # Change in time

init = input("What is the initial? (x1,y1,z1) ")
fini = input("What is the final position? (x2,y2,z2) ")

init = init.replace("(", "")
init = init.replace(")", "")
fini = fini.replace("(", "")
fini = fini.replace(")", "")

initArr = init.split(sep=",")
finiArr = fini.split(sep=",")
print(initArr, finiArr)

# Location values
x1 = float(initArr[0])
x2 = float(finiArr[1])
y1 = float(initArr[0])
y2 = float(finiArr[1])
z1 = float(initArr[0])
z2 = float(finiArr[1])

# Determine the rate of change for each x, y, and z value pairs
mx = (x2 - x1)/diffTime
my = (y2 - y1)/diffTime
mz = (z2 - z1)/diffTime

# Time that has passed
pTime = (t3-t1)

# New location values that correspond with the amount of time that has
# passed in relation to their respective rates of change
px = (pTime * mx) + x1
py = (pTime * my) + y1
pz = (pTime * mz) + z1

# Printing
print("x0: " + str(px) + " m")
print("y0: " + str(py) + " m")
print("z0: " + str(pz) + " m")