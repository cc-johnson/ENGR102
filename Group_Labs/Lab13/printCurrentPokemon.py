
# Function to print the information about the current pokemon

def printCurrentPokemon(playerID): # Anna

    print('(1) - Use Candy to Level - Up: ')        # (1) - Use Candy to Level - Up
    print('(2) - Exit to Main Menu')                # (2) - Exit to Main Menu
    choice = int(input('Enter your choice[1-2]: '))
    if choice == 1:
	    print('Use Candy to Level - Up: ')
    elif choice == 2:
	    print('Exit to Main Menu: ')

playerID = 'Ash'
printCurrentPokemon(playerID)

