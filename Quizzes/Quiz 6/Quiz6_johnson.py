# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Quiz 6
# Date:        23 October 2019
from math import sin, cos
import matplotlib.pyplot as plt

# Input for when to start and finish showing data
startDay = 0 #int(input("What is the startng day you want to plot? "))
endDay = 30 #int(input("What is the ending day you want to plot? "))

# Difference in the number of days
diffNumDays = endDay - startDay

# Generate all of the x coordinates
xCords = [i/100 for i in range(startDay*100, endDay*100, diffNumDays)]
# By multiplying the start and end days by 100 and dividing the answer by 100, I get the same thing
# as if I changed my i value by a factor that would make it so that I have 100 different data points calculated

mosquitoPop = [] # Mosquito population f(x) values
annoyanceReports = [] # Reports of annoyance f(x) values
# For loop to generate all of the y values based on the x values
for i in xCords:
    mosquitoPop.append(200 + (i**2) + (100 * sin(i)))
    annoyanceReports.append(250 + (i**2) - (215*cos(i)))

# Plot both graphs: Mosquito pop, and Reports of Annoyance with labels
plt.plot(xCords, mosquitoPop, label='Mosquito Population (100,000s)')
plt.plot(xCords, annoyanceReports, label='Reports of Annoyance')

# Draw a legend
plt.legend(loc='upper left')

# Label the axis
plt.xlabel('Day')
plt.ylabel('Number')

# Give the chart a title
plt.title('Important Fake News')

# Show the chart
plt.show()