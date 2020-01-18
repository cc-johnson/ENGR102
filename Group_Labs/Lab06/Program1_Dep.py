# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab06 Activity 1
# Date:        6 October, 2019

from math import sqrt, fabs

pokemonName = input('Enter Pokemon name: ')
combatPoints = int(input('Enter current Combat Points (CP): '))
level = int(input('Enter current level (1-40): '))
candies = int(input('Enter the current number of candies: '))

stats = [combatPoints, level, candies]          # CP is first, level is second, candy is third
# stats[0] is CP, stats[1] is level, stats[2] is candies
# Initial stat menu
print(pokemonName)
print('Current CP: ', stats[0])
print('Current Level: ', stats[1])
print('Candies: ', stats[2])
print('1 - Add Candy')
print('2 - Use Candy to Level up')
print('3 - Exit to Main Menu')

# Options set: 1 is add candy, 2 is use candy, 3 is main menu
option = int(input('Choose an option (1-3): '))

while option != 3:
    if option == 1:                                         # Add candies
        stats[2] += int(fabs(int(input('How many more candies?: '))))
    elif option == 2:                                       # Use candies
        if 1 <= stats[1] <= 30:                                # Levels 1-30
            if stats[2] >= 1:
                stats[2] -= 1
                stats[1] += 1
                stats[0] += int(stats[0] * .0094 / ((.095 * sqrt(stats[1])) ** 2))      # CP for levels 1-30
            elif stats[2] <= 0:
                print('You need more candies.')
        elif 31 <= stats[1] < 40:                              # Levels 31-40
            if stats[2] >= 2:
                stats[2] -= 2
                stats[1] += 1
                stats[0] += int(stats[0] * .0045 / ((.095 * sqrt(stats[1])) ** 2))
            elif stats[2] <= 0:
                print('You need more candies.')
        elif stats[1] == 40:                                    # Max level
            print(pokemonName + ' has reached the maximum level.')
    # New stat menu
    print(pokemonName)
    print('Current CP: ', stats[0])
    print('Current Level: ', stats[1])
    print('Candies: ', stats[2])
    print('1 - Add Candy')
    print('2 - Use Candy to Level up')
    print('3 - Exit to Main Menu')
    option = int(input('Choose an option (1-3): '))
if option == 3:
    print('Finished. Thanks for playing!')