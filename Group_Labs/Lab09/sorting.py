xVals = []
yVals = []

# This  block of code sorts the $yVals list in conjunction with the $xVals list
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