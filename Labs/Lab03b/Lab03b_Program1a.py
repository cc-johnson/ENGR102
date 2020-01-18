# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 03b Program 1a
# Date:        15 September, 2019

from math import *

# [1.d] Kinetic Energy Calculation
mass = float(input("What is the mass of the object? "))
velocity = float(input("What is the velocity the object is traveling at? ")) ** 2.0
kineticEnergy = (mass)*(velocity)/2.0
print(str(kineticEnergy))