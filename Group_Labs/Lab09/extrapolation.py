# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Anna Olmedo
# Section:     413
# Team:        23
# Assignment:  Activity 1
# Date:        21 October 2019


#Quiz over plots, need to know how to create data points, how to create plot itself, how to title and label x and y, how to create a legend

# Extrapolation Function
# K(endpoints)
# funcX (float)
# Outside Domain
# if less than the first index or greater than the last index

xVals = [5,3,5.3,7.98752,8.6,4,3.1,7,8,3]
yVals = [9, 5, 6, 3, 6, 8, 4, 7, 3, 11]
xVals.sort()
yVals.sort()

x = float(input(('Input a value for x: ')))

x1 = 0
x2 = 0
y = 0
y1 = 0
y2 = 0

if x > xVals[-1]:
    x1 = xVals[-1]
    x2 = xVals[-2]
if x < xVals[0]:
    x1 = xVals[1]
    x2 = xVals[0]

y = y1 + (((x - x1) / (x2 - x1)) * (y1 - y2))
print(y)


