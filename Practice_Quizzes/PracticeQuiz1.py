from math import *

# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Practice Quiz 1
# Date:        11 September, 2019

maxWeight_T = 9000 #tons
maxWeight_lb = 9000 * 2000 #pounds
diameter = 200 #ft
load = 120 #lb/ft^2

floorArea = pi*(100**2)
floorWeight = floorArea * load
numFloors = maxWeight_lb // floorWeight
offSpace = floorArea * float(numFloors)
totalWeight = floorWeight * numFloors

print("The foundation can hold", numFloors,"floors.")
print("This will provide", offSpace,"sqft of office space.")
print("The total weight will be", totalWeight,"tons.")