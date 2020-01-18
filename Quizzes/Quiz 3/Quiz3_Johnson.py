# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 3
# Date:        25 September, 2019

from math import *

# Prompt user for a number, taken as a float
num = float(input("Enter a number: "))

# If the float has no decimals *aside from 0* convert the float var type to an int for menu option 3 purposes
if (floor(num) - num == 0):
    num = int(num)

print()
print("--------MENU--------")
print("1 - Is the value even?")
print("2 - Is the value an integer?")
print("3 - Is the value positive?")
print("4 - If the value entered was the current temperature (F), how would I feel?")
print("5 - Quit")
print("--------------------")

# Prompt user for choice after giving menu
choice = int(input("Enter your selection: "))

# Begin comparing from the choice with respect to the menu
if choice == 1: # Check for even/odd
    if num % 2 == 0:
        print("Yes,", num, "is even.")
    else:
        print("No,", num, "is odd.")
elif choice == 2: # Check for integer vs not
    if type(num) == int:
        print("Yes,", num, "is an integer.")
    else:
        print("No,", num, "is not an integer.")
elif choice == 3: # Check for positive or negative
    if num > 0:
        print("Yes,", num, "is positive.")
    else:
        print("No,", num, "is negative.")
elif choice == 4: # Check for temperature
    if num >= 80:
        print(num, "degrees is hot.")
    elif 60 <= num < 80:
        print(num, "degrees is pretty good.")
    elif 20 <= num < 60:
        print(num, "degrees is cold.")
    elif num < 20:
        print(num, "degrees is freezing.")
elif choice == 5: # Quit
    print("Goodbye")
else:
    print("That entry is not valid")