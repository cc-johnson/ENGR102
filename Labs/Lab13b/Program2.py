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

v = np.array([[1],[0]])
m = np.array([[1.00583,-.087156],[.087156,1.00583]])

xVals = np.array([0])
yVals = np.array([1])

for i in range(200):
	v = m @ v
	xVals = np.append(xVals,v[0])
	yVals = np.append(yVals,v[1])

plt.plot(xVals, yVals)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Array multiplication')
plt.show()