# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab06 Activity 3
# Date:        6 October, 2019

import matplotlib.pyplot as plt

# Inputs for fuel cost, distance
fuelCost = float(input('How much is one gallon of gas ($/gal)? '))
distance = int(input('How far away is the destination (in miles)? '))

mphList = []
mpgList = []
costList = []
timeList = []

# for loop, nested list
for mph in range(5, 81, 5):
	mpg = -5.9852 + (1.6052 * mph) - (.0141 * (mph ** 2))
	totalCost = (distance / mpg) * fuelCost
	timeTrav = (mph / distance) ** -1
	mphList.append(round(mph,2))
	mpgList.append(round(mpg,2))
	costList.append(round(totalCost,2))
	timeList.append(round(timeTrav,2))

# Menu
print('1 - Create a table of mph, mpg, total cost, and time traveled.')
print('2 - Create a mph (25-80 mph) vs. cost plot.')
print('3 - Create a cost vs. time plot for 25-80 mph.')
print('4 - Calculate the cost and time at a specific speed.')
print('5 - Quit')
option = int(input('Choose an option from the menu above: '))

while option != 5: # Start while loop where option != 5 
	if option == 1:
		print('{:>15} {:>15} {:>15} {:>15}'.format("MPH", "MPG", "COST", "TIME"))
		for i in range(len(mphList)):
			print('{:>15} {:>15} {:>15} {:>15}'.format(mphList[i], mpgList[i], costList[i], timeList[i]))
	elif option == 2:
		xvals = costList[4:]
		yvals = mphList[4:]
		plt.plot(yvals,xvals)
		plt.show()
	elif option == 3:
		xvals = costList[4:]
		yvals = timeList[4:]
		plt.xlabel("Time (Hrs)")
		plt.ylabel("Cost ($)")
		plt.plot(yvals,xvals)
		plt.show()
	elif option == 4:
		mph = float(input("How fast do you want to go? "))
		mpg = -5.9852 + (1.6052 * mph) - .0141 * (mph ** 2)
		totalCost = (distance / mpg) * fuelCost
		timeTrav = (mph / distance) ** -1
		print("The cost is: " + str(round(totalCost,2)) + ", and the time it takes is: " + str(round(timeTrav,2)))

	# Menu
	print('1 - Create a table of mph, mpg, total cost, and time traveled.')
	print('2 - Create a mph (25-80 mph) vs. cost plot.')
	print('3 - Create a cost vs. time plot for 25-80 mph.')
	print('4 - Calculate the cost and time at a specific speed.')
	print('5 - Quit')
	option = int(input('Choose an option from the menu above: '))

	# End while loop where option != 5

print('Finished.')