# User input amount of data sets
xInput = input('Enter an x value (enter q to quit): ')
while xInput != 'q':
	yInput = float(input('Enter a y value: '))
	xVals.append(float(xInput))
	yVals.append(yInput)
	xInput = input('Enter an x value (enter q to quit): ')
# print(xVals)
# print(yVals)