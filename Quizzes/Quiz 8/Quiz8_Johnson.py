# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 8
# Date:        6 November, 2019

import csv

# Create a file obiect to take in the dat file
file = open('OrcSlayings.dat', 'r')
# Open with csv reader
csvFile = csv.reader(file)

# Create list of all the numbers in csvfile
lines = [int(line[0]) for line in csvFile]
file.close()

# Sort through the data and create averages
weeks = {}
week = 1
day = 1
weekSum = 0
for num in lines:
    if day <= 7:
        weekSum += num
        day += 1
    elif day > 7:
        weeks[week] = round(weekSum / 7, 3)
        week += 1
        day = 1
        weekSum = 0
        weekSum += num
        day += 1

if len(lines) % 7 != 0:
    weeks[week] = '(incomplete)'

# Write to new file with sorted data, use 'x+' to open in order to create the file, assuming file does not exist previously
with open('WeeklyAverages.csv', 'x+') as file:
    csvFile = csv.writer(file)
    csvFile.writerow(['Week #', 'Orcs slayed/day'])
    for week in weeks:
        csvFile.writerow([week, weeks[week]])
