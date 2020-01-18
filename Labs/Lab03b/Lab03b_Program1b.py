# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 03b Program 1b
# Date:        15 September, 2019

from math import *

# [1.e] Reynolds Number Calculation
fluidVel = float(input("What is the current fluid velocity? "))
charLinDim = float(input("What is the current characteristic of linear dimension? "))
kinVis = float(input("What is the current kinematic viscosity? "))
reynolds = fluidVel * charLinDim / kinVis
print(reynolds)