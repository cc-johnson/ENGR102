# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 06b Program 2
# Date:        6 October, 2019

# Done

import matplotlib

num = int(input("What is your starting number: ")) # Initial sequence number
sequence = [] # Initialize the sequence list

while num != 1: # Continuously run the loop until the sequence is equal to 1
	sequence.append(int(num))
	if num % 2 == 0: # Check for even
		num = num / 2 # Divide num by 2
	else: # If not even, it is odd
		num = (3 * num) + 1 # Multiply by 3 and add 1

steps = [] # Create list of step numbers
for i in range(len(sequence)):
	steps.append(i)

# Print the two lists
print(sequence)
print(steps)

# --------------------------
# Begin matplotlib and numpy
# --------------------------
import numpy
import matplotlib.pyplot as plt

# Create and show plot
plt.plot(steps, sequence) # Create line plot with yvals against xvals
plt.show() # Show the figure