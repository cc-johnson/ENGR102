# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 10 Activity 1
# Date:        03 November, 2019

# Import pylplot and such
import matplotlib.pyplot as plt

# Input file name
datFileName = input('What is the name of the file you want to use? ')

# Open the file
datFile = open(datFileName, 'r')

# Read in the file
datFileStr = datFile.readlines()

# Take the title line of the file
titleLine = datFileStr[3]

# Find out where the ------------------- are
indexOfDashes1 = datFileStr.index('-----------------------------\n')
indexOfDashes2 = datFileStr.index('-----------------------------\n', (indexOfDashes1 + 1))

# Only take the part of the list with points
datFileStr = datFileStr[indexOfDashes1 + 1:indexOfDashes2]

xVals = []
yVals = []
# Separate x and y points
for point in datFileStr:
	# Split at comma
	point = point.strip()
	point = point.split(',')

	# Take the x side
	xVal = point[0]

	# Take the y side
	yVal = point[1]

	# Remove the '('
	xVal = xVal[1:]

	# Remove the ')'
	yVal = yVal[:-1]

	# Append values
	xVals.append(float(xVal))
	yVals.append(float(yVal))

# Ask for the x val
x = float(input(('What is the value of x you are looking for? ')))
x1 = x2 = y = y1 = y2 = count = 0
used = ''
# Calculate the input x's f(x) value
if x > xVals[-1]:
	x1 = xVals[-1]
	x2 = xVals[-2]
	y = y1 + (((x - x1) / (x2 - x1)) * (y1 - y2))
	used = 'extrapolation'
elif x < xVals[0]:
	x1 = xVals[1]
	x2 = xVals[0]
	y = y1 + (((x - x1) / (x2 - x1)) * (y1 - y2))
	used = 'extrapolation'
else:
	while x > xVals [count]:
		count += 1
		y = yVals[count - 1] + (x - xVals[count-1]) * ((yVals[count] - yVals[count - 1]) / (xVals[count] - xVals[count - 1]))
		used = 'interpolation'

# Print out the calculation and what it used
print('For the x: ' + str(x) + ', f(x) = ' + str(y) + ' and it uses: ' + used)

# Generate the chart
title = titleLine.split(',')
yTitle = title[1]
xTitle = title[0]
yTitle = yTitle[yTitle.index(':')+2:]
xTitle = xTitle[xTitle.index(':')+2:]

plt.title(yTitle + " vs. " + xTitle)
plt.xlabel('Time')
plt.ylabel(yTitle)
plt.scatter(xVals, yVals, label=yTitle, color="k")
plt.plot(xVals, yVals, color="k", linewidth=1.0, linestyle="--", label="")
plt.legend(loc='upper right', frameon='True')

plt.scatter(x,y, label='Data Point', color='blue')
plt.annotate('Your data point is here:\n y=' + str(y), xy=(x, y), xycoords='data', xytext=(-75,-75), textcoords='offset points', fontsize='10', arrowprops=dict(arrowstyle="->"), color='k')
plt.plot([x,x], [0,y], color="k", linewidth=1.0, linestyle="--", label="")

# Show the chart
plt.show()