# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 4
# Date:        13 October, 2019
from random import uniform
from math import sin

print("The function being solved for is: (sin(x))/((sinx(x/10))+(x/10))")
min = float(input("What is the lower limit of your range? "))
max = float(input("What is the upper limit of your range? "))

deltRange = int(max - min)

xVals = [uniform(min, max) for i in range(deltRange)]
yVals = [round((sin(x) / (sin(x/10) + x/10)),2) for x in xVals]

# maxY = max(yVals)

print(xVals, yVals)