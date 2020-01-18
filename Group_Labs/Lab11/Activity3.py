# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 11 Activity 3
# Date:        10 November, 2019

# ATTENTION
# To make life easy, uncomment line #169 and use this link,
# with the points displayed: https://www.desmos.com/calculator/6vpmwt3sqs
# ATTENTION

# ----------------------------------------- IMPORTS STATEMENTS------------------------------------------
# Imports
from math import radians, tan, cos, sin, pi, sqrt
import random
import matplotlib.pyplot as p

# ---------------------------------------- FUNCTION DEFINITIONS-----------------------------------------
# Determine which bird to use
def birdPicker():
	# Print options
	print('(1) Red = red, small bird')
	print('(2) Chuck = yellow, small bird')
	print('(3) Bomb = black, large bird ')
	print('(4) Terence = red, large bird')

	# Input for choice
	choice = int(input('Pick your bird: '))
	
	# Determine the choice and return it's corresponding value
	if choice == 1:
		return 'Red'
	elif choice == 2:
		return 'Chuck'
	elif choice == 3:
		return 'Bomb'
	elif choice == 4:
		return 'Terence'
	else:
		return 'You decided not to pick a bird'

# Determine the planet the bird will be launched on
def planetPicker():
	# Print options
	print('(1) Earth = 9.807 m/s^2')
	print('(2) Mars = 3.711 m/s^2')
	print('(3) Moon = 1.625 m/s^2')
	print('(4) Jupiter = 24.79 m/s^2')

	# Input for choice
	choice = int(input('Pick your planet: '))
	
	# Determine the choice and return it's corresponding value
	if choice == 1:
		return 9.807
	elif choice == 2:
		return 3.711
	elif choice == 3:
		return 1.625
	elif choice == 4:
		return 24.79
	else:
		return 'You decided not to pick a planet'

# Get user guesses
def getGuesses():
	# User inputs for guesses
	inVel = float(input("What is " + bird + "'s initial velocity? "))
	theta = float(input("At what angle should " + bird + " be shot at? "))
	
	# Return the guesses
	return inVel, theta

# Calculate the x and y values for the trajectory based on the guesses given by user
def trajectory(g, vGuess, thetaGuess):
	# Convert thetaGuess into radians
	thetaGuess = radians(thetaGuess)
	# Determine velocity in the x and y
	Vx = vGuess * cos(thetaGuess)
	Vy = vGuess * sin(thetaGuess)

	# Calculates time it takes to land on ground with no incident
	t = 0
 
	xVals = []
	yVals = []
	# Calculate the x and y values for each time
	while ((Vy * t) - (g * (t**2) / 2)) >= 0:
		t += .1
		xVals.append(Vx*t)
		yVals.append((Vy * t) - (g * (t**2) / 2))
	# Return lists of x and y values
	return xVals, yVals

# Determine if the pig has been hit
def hit(xVals, yVals, target):
	# Starting values
	willHit = False
	hitZone = (0,0)
	# For the length of the $xVals list
	for i in range(len(xVals)):
		# If the distance between the point and the center of the pig's location is less than the radius and the point 
		# is within the pig's 'square' (basically a square with sides of 2*radius around the center of the pig's circle)
		if sqrt((target[1] - yVals[i]) * (target[1] - yVals[i]) + (target[0] - xVals[i]) * (target[0] - xVals[i])) < target[2] and target[0] - target[2] < xVals[i] < target[0] + target[2] and target[1]-target[2] < yVals[i] < target[1]+target[2]:
			willHit = True
			hitZone = (xVals[i],yVals[i])
			# If hit, end the loop
			break
		# Change 'hitZone' to the birds final location in the loop unless it quits
		hitZone = (xVals[i],yVals[i])
	# Return whether the pig has been hit and where it was hit
	return willHit, hitZone

# Plot everything
def birdsPlot(xVals, yVals, targ, bird, hitZone=(0,0), hit=False):
	pig = p.Circle((targ[0],targ[1]),targ[2], color='green')
	birdColor = 'red'
	if bird == 'Red':
		birdColor = 'red'
	if bird == 'Chuck':
		birdColor = 'yellow'
	if bird == 'Bomb':
		birdColor = 'black'
	if bird == 'Terence':
		birdColor = 'red'

	if impact == True:
		ind = -2
		for i in range(len(xVals)):
			if xVals[i] < hitZone[0] < xVals[i+1]:
				ind = i
		p.plot(xVals[:i+1],yVals[:i+1])
		birdCirc = p.Circle((hitZone[0],hitZone[1]),2, color=birdColor)
	else:
		p.plot(xVals,yVals)
		birdCirc = p.Circle((hitZone[0],0),2, color=birdColor)

	p.gcf().gca().add_artist(pig)
	p.gcf().gca().add_artist(birdCirc)
	p.xlim(float(0),float(targ[0])+2*float(targ[2]))
	p.ylim(float(0),float(targ[1])+2*float(targ[2]))
	p.show()

def getBasics():
	"""Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes name,
	color and size. 'Planet' includes name and gravity. """
	a = birdPicker() # Runs fn to provide bird menu
	b = planetPicker() # Runs fn to provide planet menu
	return a, b

def trajectoryY(x, g, vo, angle):
	"""Returns (y-value) of the trajectory for a given x-value, gravity, initial velocity, and angle."""
	angle = radians(angle)
	return (x*tan(angle))-(g*x**2)/(2*(vo**2)*cos(angle)**2)

# -------------------------------------------- MAIN PROGRAM --------------------------------------------
# (Then your Main Program)

# Sets up loop so user can repeat the game as many times as desired ('y' to continue, 'n' to quit)
pigCounter = 0
again = 'y'
while again == 'y':
	# Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
	target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))
	print('target location:', target) # UNCOMMENT ME if you want to see where the target is before it gets drawn
	
	# Takes initial guesses
	bird, g = getBasics() # Runs fn to get bird and planet (gravity)
	vGuess, thetaGuess = getGuesses() # Runs fn to get initial velocity and angle guesses
	
	# Loops guesses until bird hits target
	x, y = trajectory(g, vGuess, thetaGuess) # Create current x- and y- value lists
	impact, hitZone = hit(x, y, target)
		
	while not impact: # Program cycles until throw hits the target
		birdsPlot(x, y, target, bird, hitZone, impact) # Plots trajectory & target of miss
		vGuess, thetaGuess = getGuesses() # Gets updated guesses from user
		x, y = trajectory(g, vGuess, thetaGuess) # Creates updated lists of x- and y-values
		impact, hitZone = hit(x, y, target)
	
	# Handles winning case and asks if user would like to play again
	print('Yay!')
	pigCounter += 1
	birdsPlot(x, y, target, bird, hitZone, impact)
	again = input('Would you like to play again? (y/n)')
	while again not in {'y', 'n'}:
		again = input('Please type either y or n only. Would you like to play again? (y/n)')

# Exiting when user decides to quit
print('\nThanks for playing! You popped %d pig(s) today!' % pigCounter)