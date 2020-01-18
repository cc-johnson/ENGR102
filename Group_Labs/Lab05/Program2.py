# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Chase Johnson, Bryan Jones, Anna Olmedo
# Section:     413
# Assignment:  Lab Assignment 5, Activity 1
# Date:        23 September 2019

# Initial time is zero seconds and other constants
time = 0
count = 0
bananas = 0

# Input acceleration
acceleration = float(input('What is the acceleration?: '))

# Other initial kinematic values
velocity = 0
distance = 0

while (distance <= 500) and (velocity <= 88) and (time <= 10):
    time += .01
    velocity = (acceleration * time) / 1.467    # Converting from ft/s to mph
    distance = .5 * acceleration * (time ** 2)
    count += 1

bananas = count // 120

if (velocity >= 88) and (acceleration <= 16):
    print('Success!')
else:
    print('Failure...')

print('The velocity is ', velocity, 'mph. ', 'The distance traveled is ', distance, ' feet. ', '\n')
print('The time elapsed is ', time, ' seconds. ', 'There are ', bananas, ' bananas.')