# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 06b Program 1
# Date:        6 October, 2019

# Needs the table to be finished

from numpy import mean

measurements = [15.80, 19.60, 21.85, 33.61, 49.73, 51.27, 56.26, 63.06, 76.56, 76.57, 85.78, 90.74, 92.60, 99.71,100.51, 101.12, 101.25, 102.19, 104.85, 110.59, 125.92, 131.25, 136.04, 141.15, 148.54, 150.02]

# Appending 162.76 to measurements
measurements.append(162.76)

# Insert 71.01 into index 8 (position 9)
measurements.insert(8,71.01)

# Print the "number of days" (length of list)
print(len(measurements))

# Find the average of the list
print(sum(measurements)/len(measurements))

# Compute the means of weeks
meanWeek1 = round(mean(measurements[0:7]), 2)
meanWeek2 = round(mean(measurements[7:14]), 2)
meanWeek3 = round(mean(measurements[14:21]), 2)
meanWeek4 = round(mean(measurements[21:28]), 2)

# Compute the rates of weeks
rateWeek1 = round((measurements[6] - measurements[0]) / 7, 2)
rateWeek2 = round((measurements[13] - measurements[7]) / 7, 2)
rateWeek3 = round((measurements[20] - measurements[14]) / 7, 2)
rateWeek4 = round((measurements[27] - measurements[21]) / 7, 2)

# Print everything
print("\n\nThere were", len(measurements), "days of data measurements taken.")
print("----------------------------------------------------")
print("Average moss mass in week 1:", meanWeek1)
print("Average moss mass in week 2:", meanWeek2)
print("Average moss mass in week 3:", meanWeek3)
print("Average moss mass in week 4:", meanWeek4)
print("----------------------------------------------------")
print("Average growth in week 1:", rateWeek1)
print("Average growth in week 2:", rateWeek2)
print("Average growth in week 3:", rateWeek3)
print("Average growth in week 4:", rateWeek4)