# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 10 Activity 2
# Date:        03 November, 2019

# Import csv package
import csv

dates = []

maxTemps = []
minTemps = []

humidity = []
pressure = []

precipitation = []

# Open the file
with open('WeatherDataWindows(1).csv', 'r') as file:
	csvFile = csv.reader(file, delimiter=',')
	csvFile = [row for row in csvFile]
	csvFile = csvFile[1:]
	for row in csvFile:
		dates.append(row[0])
		maxTemps.append(int(row[1])) # High temps
		minTemps.append(int(row[3])) # Low temps
		humidity.append(int(row[8]))
		pressure.append(float(row[11]))
		precipitation.append(float(row[-1]))

# Find the values called for by the lab
# Max/min temps
maxTemp = max(maxTemps)
minTemp = min(minTemps)
print(minTemp, maxTemp)

# Average Precipitation
avgPrecipitation = sum(precipitation)/len(precipitation)
print(avgPrecipitation)

# Average Humidity
avgHumidity = sum(humidity)/len(humidity)
print(avgHumidity)

# Find the average pressure in June 2016
startIndexOfJune2016 = dates.index('6/1/2016')
endIndexOfJune2016 = dates.index('7/1/2016')
avgPressureJune2016 = sum(pressure[startIndexOfJune2016:endIndexOfJune2016])/len(pressure[startIndexOfJune2016:endIndexOfJune2016])

# print(startIndexOfJune2016, endIndexOfJune2016, avgPressureJune2016)

# Print the values
print('------------------')
print('Maximum Temperature: %d F' % maxTemp)
print('Minimum Temperature: %d F' % minTemp)
print('Average Daily Precipitation: %4.2f in' % avgPrecipitation)
print('Average Daily Humidity: %4.2f' % avgHumidity)
print('Average Pressure during June 2016: %4.2f mmHg' % avgPressureJune2016)