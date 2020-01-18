# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 10b Program 3
# Date:        3 November, 2019

import matplotlib.pyplot as plt
import csv

xVals = []
yVals = []
# Open the csv file
with open('loan.csv','r') as file:
	# Read the csv file
	csvFile = csv.reader(file, delimiter=',')
	csvFile = [row for row in csvFile]
	csvFile = csvFile[1:]
	# Go through every row of the csv file and append stuff
	for row in csvFile:
		if len(row) > 1:
			xVals.append(float(row[0]))
			yVals.append(float(row[1]))
	if csvFile[-1][0] != '30':
		xVals.append(10)
		yVals.append(0)

# Generate the chart
xTitle = 'Month'
yTitle = 'Principal Balance'

plt.title('Amortization Schedule')
plt.xlabel(xTitle)
plt.ylabel(yTitle)
plt.scatter(xVals, yVals, label='Amortization Schedule', color="k")
plt.plot(xVals, yVals, color="k", linewidth=1.0, linestyle="--", label="")
plt.legend(loc='upper right', frameon='True')

# Show the chart
plt.show()