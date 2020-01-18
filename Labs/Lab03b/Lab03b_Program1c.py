# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 03b Program 1c
# Date:        15 September, 2019

from math import *

# [1.f] Energy Radiated per Unit Surface Area Calculation
constProp = float(input("What is the constant of proportionality? "))
absTemp = float(input("What is the absolute temperature of the object? "))
radiated = constProp * (absTemp ** 4.0)
print(radiated)