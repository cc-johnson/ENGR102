# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 11b Program 1
# Date:        10 November, 2019

def findLeastProfit(names, productValue, operationalCost):
	profitabiliy = []

	# For each of the factories, calculate the productivity
	for i in range(len(names)):
		profitabiliy.append(productValue[i] - operationalCost[i])

	# Determine the least productive factory
	leastProfitable = names[profitabiliy.index(min(profitabiliy))]

	# return the least profitable factory
	return leastProfitable, min(profitabiliy)