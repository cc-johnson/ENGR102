# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Anna Olmedo, Chase Johnson, Bryan Jones
# Section:     413
# Assignment:  Lab Assignment 8, Activity 1
# Date:        14 October 2019

from matplotlib.pyplot import *
import math

# ---------------
# Plot 1
# ---------------
subplot(2,1,1)

t = []
y1 = []
y2 = []

for i in range(0, 153, 3):
    i /= 50
    t.append(i)
    y1.append(i ** 2 * math.exp(-i ** 2))
    y2.append(i ** 4 * math.exp(-i ** 2))

# Data points
x = [0, .45, 1.1, 1.75, 2.25, 2.7]
y = [0, .23, .4, .18, .07, .01]

scatter(x, y, color='black', label='data')
plot(t, y1, color="red", linewidth=1.0, linestyle="-", label="t^2exp(-t^2)")
plot(t, y2, color="blue", linewidth=1.0, linestyle="-", label="t^4exp(-t^2)")

# Plot and axes titles
title('Data and two curves vs. time')
xlabel('time')
ylabel('y')

legend(loc='upper right')

# Set intervals
yticks([0.00, .25, .5, .75, 1.00])
xticks([0.0, .5, 1.0, 1.5, 2.0, 2.5, 3.0])

# ---------------
# Plot 2
# ---------------

subplot(2,1,2)

t = []
y1 = []

for i in range(0, 153, 3):
    i /= 50
    t.append(i)
    y1.append(i ** 2 * math.exp(-i ** 2))

# Data points
x = [.45, 1.1, 1.75, 2.25]
y = [.23, .4, .18, .07]

plot(x, y, color='yellow', label='data')
plot(t, y1, color='blue', linewidth=1.0, linestyle="-", label="t^2exp(-t^2)")
axis([1, 2, 0, 0.5])

scatter(x[1:3], y[1:3], color='yellow', marker='^')

# Plot and axes titles
title('Data interpolation and Curve 1')
xlabel('time')
ylabel('y')

legend(loc='upper right')

# Set intervals
yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
xticks([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])

annotate("It\'s closest here!", xy=(1.4,.3), xycoords='data', xytext=(-80,-70), textcoords='offset points', fontsize='10', arrowprops=dict(arrowstyle="->"))

show()