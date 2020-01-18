# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson, Anna Olmedo, Bryan Jones, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 02
# Date:        5 September, 2019

from math import *

# Set values
xi = 30 # Starting time
yi = 50 # Starting position
y = 50
xf = 45 # Final time
yf = 615 # Final position

# T = 37s
x = 37 # Current time
y = yi + (x - xi)*((yf-yi)/(xf-xi)) # Current position
print("Time: 37, Position: " + str(y))