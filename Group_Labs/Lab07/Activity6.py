# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 6
# Date:        13 October, 2019

# Input for how many days of production
numDays = int(input("How many days would you like to report? "))

productionDays = []
# Takes input for each day of production
for i in range(numDays):
	productionForDay = int(input("What was the production for day " + str(i+1) + "? "))
	productionDays.append(productionForDay)

# List to contain sublists for each type of interval
intervals = []
for i in range(numDays-1):
	intervals.append([])

# For loop to determine which days were better/worst than the last 
for i in range(len(intervals)):
	count = 0
	for j in range(len(productionDays)-(i+1)):
		difference = productionDays[(i+j)+1] - productionDays[j]
		if difference < 0:
			intervals[i].append(-1)
		elif difference > 0:
			intervals[i].append(1)
		elif difference == 0:
			intervals[i].append(0)

print()
# For each type of interval, determine the statistics
for i, interval in enumerate(intervals):
	posCount = 0
	negCount = 0
	for j in interval:
		if j > 0: posCount += 1
		elif j <0: negCount -= 1

	# Print the final stats for each interval
	print("For " + str(i+1) + "-day intervals " + str(round(posCount/len(intervals[i]),2)*100) + "% were increasing and " + str(round(negCount/len(intervals[i]),2)*100) + "% were decreasing")