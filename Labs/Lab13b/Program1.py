# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 13b Program 1
# Date:        24 November, 2019
import numpy as np
import matplotlib.pyplot as plt

"""Write a program to plot y1 = sin(x) and y2 = cos(x) versus x on the same plot for the domain 0 ≤ x ≤ 4π. Also,
plot the points where the two curves intersect with an asterisk or some other marker, that is, where sin(x)
= cos(x). Recall that sin(x) = cos(x) for x = π/4 ± πk.
Use the numpy and matplotlib packages to create the points and plot the following figure"""

xArr = np.linspace(0,4*np.pi,1000)
sinArr = np.sin(xArr)
cosArr = np.cos(xArr)

intersectX = np.arange(4,dtype='float64')
intersectX *= np.pi
intersectX += np.pi/4

intersectY = np.sin(intersectX)

plt.plot(xArr, cosArr)
plt.plot(xArr, sinArr)
plt.scatter(intersectX, intersectY)
plt.title('Plot of cos(x) and sin(x)')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
