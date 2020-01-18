# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Chase Johnson, Bryan Jones, Anna Olmedo
# Section:     413
# Assignment:  Lab Assignment 5, Activity 1
# Date:        23 September 2019

# Initial numbers
num1 = 0
num2 = 1

# User inputs next number of Fibonacci sequence
userInput = int(input('What is the next number in the sequence?: '))

while userInput == num1 + num2:
    print('Correct.')
    num1 = num2
    num2 = userInput
    userInput = int(input('What is the next number in the sequence?: '))

print('Incorrect.')
