# Function to print the main menu
def printMenu(): # Anna

    print('(1) Print your pokemon')                         # print (1) Print your pokemon
    print('(2) Print currently selected pokemon: ')         # print (2) Print currently selected pokemon
    print('(3) Catch a new pokemon: ')                      # print (3) Catch a new pokemon
    print('(4) Level currently selected pokemon: ')         # print (4) Level currently selected pokemon
    print('(5) Battle another player: ')                    # print (5) Battle the another player
    print('(6) Switch to a different player: ')             # print (6) Switch to a different player
    choice = int(input('Enter your choice[1-6]: '))

    if choice == 1:
        print('Print your pokemon: ')
    elif choice == 2:
        print('Print currently selected pokemon: ')
    elif choice == 3:
        print('Catch a new pokemon: ')
    elif choice == 4:
        print('Level currently selected pokemon: ')
    elif choice == 5:
        print('Battle another player: ')
    elif choice == 6:
        print('Switch to a different player: ')
    return choice

printMenu()

# Provide user with option

	# return userChoice
