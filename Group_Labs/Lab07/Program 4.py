# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Anna Olmedo, Chase Johnson, Bryan Jones
# Section:     413
# Assignment:  Lab Assignment 7, Activity 2
# Date:        7 October 2019

# Quadratic function (x ** 2) - (10 * x) + 25
print('x^2 - 10x + 25')

# User input x interval
minX = int(input('Enter an integer: '))
maxX = int(input('Enter an integer higher than before: '))

# find zeros of func
zeros = []
for i in range(minX, (maxX + 1), .01):
    if ((i ** 2) - (10 * i) + 25) == 0:
        zeros.append(i)
maxZero = max(zeros)
print('The maximum value of the function is,', maxZero)
print('The solutions of the function are x =', zeros)

