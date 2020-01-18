# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 04b Program 2
# Date:        22 September, 2019

from math import *

fluidVel = float(input("What is the current fluid velocity? "))
charLinDim = float(input("What is the current characteristic of linear dimension? "))
kinVis = float(input("What is the current kinematic viscosity? "))
reynolds = fluidVel * charLinDim / kinVis

# Reference Material
# https://ocw.mit.edu/courses/mechanical-engineering/2-000-how-and-why-machines-work-spring-2002/study-materials/TurbulentFlow.pdf

if reynolds > 4000.0:
	print("Turbulent flow")
elif reynolds > 2100.0:
	print("Transition flow")
elif reynolds > 0.0:
	print("Laminar flow")
else:
	print("Not valid inputs, result is: " + str(reynolds))