xVals = []
yVals = []

x = float(input(('What is the value of x you are looking for? ')))
units = input('What is the dependant variable? ')

addX = input(('Enter an x value (enter q to quit): '))
# User input amount of data sets
while addX != 'q':
	addY = float(input('Enter a y value: '))
	xVals.append(float(addX))
	yVals.append(addY)
	addX = input('Enter an x value (enter q to quit): ')

# This block of code sorts the $yVals list in conjunction with the $xVals list
for i in range(len(xVals)): # Iterate through the $xVals list
	for j in range(len(xVals)): # Iterate through the $xVals list
		if xVals[i] < xVals[j]: # If the $x at $xVals[i] is less than the $x at $xVals[j], swap them
			# Move $x to new location with new index
			tmpX = xVals[j]
			xVals[j] = xVals[i]
			xVals[i] = tmpX

			# Move $y to new location with the new $x index
			tmpY = yVals[j]
			yVals[j] = yVals[i]
			yVals[i] = tmpY

x1 = x2 = y = y1 = y2 = count = 0
if x > xVals[-1]:
	x1 = xVals[-1]
	x2 = xVals[-2]
	y = y1 + (((x - x1) / (x2 - x1)) * (y1 - y2))
elif x < xVals[0]:
	x1 = xVals[1]
	x2 = xVals[0]
	y = y1 + (((x - x1) / (x2 - x1)) * (y1 - y2))
else:
	while x > xVals [count]:
		count += 1
	y = yVals[count - 1] + (x - xVals[count-1]) * ((yVals[count] - yVals[count - 1]) / (xVals[count] - xVals[count - 1]))

with open('nailedIt.txt', 'r+') as file:
	file.write('Team 23:\tBryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez\n')
	file.write('Date: 27 October 2019\n')
	file.write('\n')
	file.write('The x values represent: time, and the y values represent: ' + units + '\n')
	file.write('-----------------------------\n')
	for i in range(len(xVals)):
		file.write('(' + str(xVals[i]) + ',' + str(yVals[i]) + ')\n')
	file.write('-----------------------------\n')

	x = input(('What is the value of x you are looking for? '))
	# User input amount of data sets
	while x != 'q':
		x = float(x)
		x1 = x2 = y = y1 = y2 = count = 0
		used = ''
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
		file.write('(' + str(x) + ',' + str(y) + '): ' + used + '\n')
		x = input(('What is the value of x you are looking for? '))