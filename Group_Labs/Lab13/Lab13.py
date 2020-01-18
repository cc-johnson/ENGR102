from math import sqrt
from random import randint
import csv

def printPlayerMenu(playerID): # TODO
	print('(1) Show stored pokemon')
	print('(2) Show your current pokemon')
	print('(3) Change your current pokemon')
	print('(4) Catch a new pokemon')
	print('(5) Battle another player')
	print('(6) Switch players')
	print('(7) Create a new player')
	print('(8) Delete a player')
	print('(9) Exit and save the game')
	choice = intUserInput('Enter your choice[1-9]: ')

	playerNames = list(gameData.keys())
	if choice == 1:
		printStoredPokemon(playerID)
		return 0
	elif choice == 2:
		printCurrentPokemon(playerID)
		return 0
	elif choice == 3:
		switchCurrentPokemon(playerID)
		return 0
	elif choice == 4:
		newPokemon = catchNewPokemon()
		try:
			addPokemonToPlayer(playerID, newPokemon[0][0], [1, int(newPokemon[0][1])])
			addCandies(playerID, newPokemon[1])
		except:
			print('Sorry you did not catch a new pokemon, try again!')
		return 0
	elif choice == 5:
		print('Pick a player to battle:')
		listPlayers(True)
		userChoice = intUserInput('Which player would you like to fight? ')
		fighters = {playerID: getCurrentPokemon(playerID), playerNames[userChoice - 1]: getCurrentPokemon(playerNames[userChoice - 1])}
		winner = battle(getStats(playerID, getCurrentPokemon(playerID)), getStats(playerNames[userChoice - 1], getCurrentPokemon(playerNames[userChoice - 1])))
		if winner == 0:
			print('It\'s a tie!')
		elif winner == 1:
			print(playerID + ' wins!')
		elif winner == 2:
			print(playerNames[userChoice - 1] + ' wins!')
		return 0
	elif choice == 6:
		print('Change profiles:')
		return 2
	elif choice == 7:
		playerName = input("What should the name of this new player be? ")
		addNewPlayer(playerName)
		return 0
	elif choice == 8:
		print("What is the name of the player you want to remove? ")
		numPlayers = listPlayers(True)
		userChoice = intUserInput('Pick from the above list (enter any other number to cancel): ')
		if 1 <= userChoice <= numPlayers:
			return deletePlayer(playerNames[userChoice - 1], playerID)
		else:
			return 0
	elif choice == 9:
		saveGame()
		return -1

def listPlayers(numsOn = False):
	if numsOn == False:
		for player in gameData:
			printPlayer(player)
	else:
		count = 1
		for player in gameData:
			printPlayer(player, count)
			count += 1
		return count

def printPlayer(playerID, count = -1):
	if count == -1:
		print('------------------------------')
		print('   Name: ' + playerID)
		print('Pokemon: ')
		printCurrentPokemon(playerID, False)
		print('------------------------------')
		print()
	else:
		print('------------------------------')
		print('        Player #' + str(count))
		print('   Name: ' + playerID)
		print('Pokemon: ')
		printCurrentPokemon(playerID, False)
		print('------------------------------')
		print()

def printCurrentPokemon(playerID, opts = True): # DONE
	currentPokemonName = gameData[playerID][2]
	currentPokemonStats = gameData[playerID][0][currentPokemonName]
	print()
	print('   Pokemon Name: ' + currentPokemonName)
	print('Pokemon\'s level: ' + str(currentPokemonStats[0]))
	print('   Pokemon\'s CP: ' + str(currentPokemonStats[1]))
	if opts == True:
		print('(1) Use Candy to Level Up this pokemon: ')
		print('(2) Exit to Main Menu')
		choice = intUserInput('Enter your choice: ')
		if choice == 1:
			levelPokemon(playerID, currentPokemonName)
		elif choice == 2:
			pass
		else:
			print('That\'s not a valid choice, retrying menu option')
			printCurrentPokemon(playerID)

def printStoredPokemon(playerID, numsOn = False):
	"""Function to print the players stored pokemon,
	   and menu asscocaited with it"""
	# for each pokemon:
	playerPokemon = gameData[playerID][0]
	if numsOn == False:
		for pokemon in playerPokemon.items():
			pokemonName = pokemon[0]
			stats = pokemon[1]
			printPokemon(pokemonName, stats)
	else:
		count = 1
		for pokemon in playerPokemon.items():
			pokemonName = pokemon[0]
			stats = pokemon[1]
			printPokemon(pokemonName, stats, count)
			count += 1

def printPokemon(pokemonName, stats, count = -1):
	if count == -1:
		print('------------------------------')
		print(' Name: ' + pokemonName)
		print('Level: ' + str(stats[0]))
		print('   CP: ' + str(stats[1]))
		print('------------------------------')
		print()
	else:
		print('------------------------------')
		print(' Pokemon #' + str(count))
		print(' Name: ' + pokemonName)
		print('Level: ' + str(stats[0]))
		print('   CP: ' + str(stats[1]))
		print('------------------------------')
		print()

def pickNewPokemon(playerID):
	"""Function to choose a new active pokemon"""
	# Print list of stored pokemon
	numPokemon = len(gameData[playerID][0])
	printStoredPokemon(playerID, True)
	userChoice = intUserInput('Please pick the number for the pokemon you want to switch to: ')
	
	playerPokemon = list(gameData[playerID][0].keys())
	newSelectedPokemon = playerPokemon[userChoice-1]
	setCurrentPokemon(playerID, newSelectedPokemon)

def calcFightValue(level = 1, cp = 10): # DONE
	"""Function to calculuate the fightValue of an individual pokemon"""
	randomNum = randint(1,50)
	print(level, cp)
	fightVal = int(cp) * randomNum / int(level)
	return fightVal

def calcCP(playerID, pokemonName): # DONE
	"""Function to determine the currentCP level of the pMon"""
	stats = getStats(playerID, pokemonName)
	level = stats[0]
	currCP = stats[1]
	minCP = stats[2]
	if level <= 30:
		CP = minCP + round((currCP*.0094)/((.095*sqrt(level))**2),4)
	elif 30 < level <= 40:
		CP = minCP + round((currCP*.0045)/((.095*sqrt(level))**2),4)
	else:
		CP = currCP
	return CP

def levelPokemon(playerID, pokemonName): # DONE
	"""Function to calculate the pokemon's level-up capability
	   based on player's candies, pokemon's CP"""
	level = gameData[playerID][0][pokemonName][0]
	cp = gameData[playerID][0][pokemonName][1]
	mincp = gameData[playerID][0][pokemonName][2]
	candies = int(gameData[playerID][1])
	if level <= 30 and candies > 0 and level + candies <= 30: 
		level += candies
		candies = 0
	elif level <= 30 and candies > 0 and level + candies >= 30:
		more30 = level + candies - 30
		levelsOver30 = more30 // 2
		candies = more30 % 2
		level = 30 + levelsOver30
	elif 30 < level < 40 and candies > 1 and 30 < level + candies:
		if candies <= 20:
			level += candies // 2
			candies = candies % 2
		else:
			level = 40
			candies = 0
	
	if level > 40:
		level = 40
	
	setStats(playerID, pokemonName, level, calcCP(playerID, pokemonName))

def addPokemonToPlayer(playerID, pokemonName, pokemonStats): # DONE
	gameData[playerID][0][pokemonName] = pokemonStats

def getCurrentPokemon(playerID):
	return gameData[playerID][2]

def switchCurrentPokemon(playerID):
	print('Pick from the following list: ')
	printStoredPokemon(playerID, True)
	userChoice = intUserInput('Which of the above do you choose? ')
	pokemonNames = list(gameData[playerID][0].keys())
	gameData[playerID][2] = pokemonNames[userChoice - 1]

def getStats(playerID, pokemonName = ''): # DONE
	# try:
	if pokemonName == '':
		pokemonName = getCurrentPokemon(playerID)
	level = gameData[playerID][0][pokemonName][0]
	cp = gameData[playerID][0][pokemonName][1]
	mincp = gameData[playerID][0][pokemonName][2]
	return (level, cp, mincp)
	# except:
	# 	print(playerID, pokemonName)
	# 	return "Something went wrong getting stats"

def setStats(playerID, pokemonName, level = 1, cp = 100, mincp = 100): # DONE
	try:
		gameData[playerID][0][pokemonName][0] = level
		gameData[playerID][0][pokemonName][1] = cp
		gameData[playerID][0][pokemonName][2] = mincp
	except:
		return "Something went wrong setting stats"

def getCandies(playerID, candies): # DONE
	return gameData[playerID][1]

def setCandies(playerID, candies): # DONE
	gameData[playerID][1] = candies

def setCurrentPokemon(playerID, pokemonName): # DONE
	gameData[playerID][2] = pokemonName

def addCandies(playerID, candies = 0): # DONE
	gameData[playerID][1] += candies

def battle(pMon1, pMon2): # DONE
	"""Function to determine the winner of a battle
	   based on each pokemon's fight value"""
	pMon1FV = calcFightValue(pMon1[0], pMon1[1])
	pMon2FV = calcFightValue(pMon2[0], pMon2[1])
	if pMon1FV == pMon2FV:
		return 0
	elif pMon1FV > pMon2FV:
		return 1
	elif pMon2FV > pMon1FV:
		return 2
	else:
		return -1

def catchNewPokemon(): # DONE
	"""Function to start a minigame to 'catch' a new pokemon. If player wins, award candies"""
	user = RPS()        # RPS function use to determine if player will receive a pokemon and candies
	if user == True:
		newPoke = selectNewPokemon()
		# random generator/ conditional statement to determine how many candies the player will receive
		RandomCandies = randint(0, 2)
		if RandomCandies == 0:
			RandomCandies = 3
		elif RandomCandies == 1:
			RandomCandies = 5
		elif RandomCandies == 2:
			RandomCandies = 10
		return(newPoke, RandomCandies)      # Not sure how to put them in the dictionary but these are the variables

def RPS(): # DONE
	"""Function to play rock paper scissors (RPS)"""
	print("Time to play rock, paper, scissors against Professor Oak!")
	print("Fight Professor Oak in a best of 3 match-up to win a new Pokemon and earn more candies.")
	print("1:\t Rock")
	print("2:\t Paper")
	print("3:\t Scissors")
	Player = intUserInput("Type in a number that corresponds to the weapon you want to choose: ")
	while Player < 1 or Player > 3:
		Player = intUserInput("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: ")
	Oak = randint(1, 3)
	games = 0
	userWin = 0
	userLoss = 0
	while games < 3:
		if (Player == 1 and Oak == 3) or (Player == 2 and Oak == 1) or (Player == 3 and Oak == 2):
			print("Player wins this round!")
			print("1:\t Rock")
			print("2:\t Paper")
			print("3:\t Scissors")
			playerCont = False
			while playerCont == False:
				Player = intUserInput("Type in a number that corresponds to the weapon you want to choose: ")
				if Player < 1 or Player > 3:
					print("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: ")
				else:
					playerCont = True
			Oak = randint(1, 3)
			userWin += 1
			games += 1
		elif (Player == 3 and Oak == 1) or (Player == 1 and Oak == 2) or (Player == 2 and Oak == 3):
			print("Professor Oak wins this round!")
			print("1:\t Rock")
			print("2:\t Paper")
			print("3:\t Scissors")
			playerCont = False
			while playerCont == False:
				Player = intUserInput("Type in a number that corresponds to the weapon you want to choose: ")
				if Player < 1 or Player > 3:
					print("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: ")
				else:
					playerCont = True
			Oak = randint(1, 3)
			userLoss += 1   # Used userLoss so game won't keep on going
			games += 1
		elif Player == Oak:
			print("It's a tie! Try again")
			print("1:\t Rock")
			print("2:\t Paper")
			print("3:\t Scissors")
			playerCont = False
			while playerCont == False:
				Player = intUserInput("Type in a number that corresponds to the weapon you want to choose: ")
				if Player < 1 or Player > 3:
					print("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: ")
				else:
					playerCont = True
			Oak = randint(1, 3)
	if userWin >= 2:
		print("Congratulations!! You have defeated Professor Oak in Rock, Paper, Scissor!!")
		return True
	elif userLoss >= 2:
		print("Sorry, Try again Later!!")
		return False

def selectNewPokemon(): # DONE
	pokemon = [] # List to hold all pokemon
	with open('PokeList.csv', 'r') as file:     # for loop to only read the information and not the headers
		csvFile = csv.reader(file,delimiter=',')
		csvFile = [row for row in csvFile]
		csvFile = csvFile[1:]
		for row in csvFile:
			pokemon.append((row[1],row[2]))
		userPick = []                   # List to only hold 5 random pokemon for player to choose
		for i in range(5):
			randomSamp = randint(0, 148) # Program chooses of number at random to determine the index to choose from
			userPick.append(pokemon[randomSamp])
		print("Pick one pokemon from the 5 pokemon below by typing their corresponding number.")
		print("(1) Pokemon name: " + userPick[0][0] + ' with CP: ' + userPick[0][1])
		print("(2) Pokemon name: " + userPick[1][0] + ' with CP: ' + userPick[1][1])
		print("(3) Pokemon name: " + userPick[2][0] + ' with CP: ' + userPick[2][1])
		print("(4) Pokemon name: " + userPick[3][0] + ' with CP: ' + userPick[3][1])
		print("(5) Pokemon name: " + userPick[4][0] + ' with CP: ' + userPick[4][1])
		pokeNum = -1
		while (pokeNum < 1) or (pokeNum > 5):
			pokeNum = intUserInput("Type a number from (1-5) to pick a pokemon. ")
		return userPick[pokeNum - 1]

def addNewPlayer(playerName): # DONE
	# Allow to pick a pokemon out of 5
	pokemon = selectNewPokemon()
	pokemonData = {pokemon[0]:[1, int(pokemon[1]), int(pokemon[1])]}
	candies = randint(0,5)
	currentPokemon = pokemon[0]
	gameData[playerName] = [pokemonData, candies, currentPokemon]

def deletePlayer(playerName, currPlayer): # DONE
	if playerName != currPlayer:
		del gameData[playerName]
		return 0
	else:
		confirm = input('Are you sure you want to delete your currently selected profile (y/n) ')
		if 'y' in confirm:
			del gameData[playerName]
			return 1
		else:
			print('Very well, try picking a different player this time: ')
			playerNames = list(gameData.keys())

			print("What is the name of the player you want to remove? ")
			listPlayers(True)
			userChoice = intUserInput('Pick from the above list: ')
			deletePlayer(playerNames[userChoice - 1], currPlayer)

def changePlayer(): # DONE
	playerNames = list(gameData.keys())
	print('Which player would you like to become? ')
	listPlayers(True)
	userChoice = intUserInput('Select an above player: ')
	return playerNames[userChoice - 1]

def intUserInput(question = 'Please input your answer'): # DONE
	cont = False
	while cont != True:
		try:
			userInput = int(input(question))
			cont = True
		except:
			print("That's not an integer, please try again")
	return userInput

def saveGame(): # DONE
	with open('saved_game.csv', 'w+') as gameSave:
		csvFile = csv.writer(gameSave, delimiter=',',lineterminator='\n')
		data = gameData.items()
		for player in data:
			csvFile.writerow(player)

def openGameSave(privs): # DONE
	with open('./saved_game.csv', privs) as gameSave:
		csvFile = csv.reader(gameSave)
		for line in csvFile:
			playerName = line[0]
			playerData = line[1]
			splitPlayerData = playerData.split('}')
			pokemonData = splitPlayerData[0]
			pokemonData = pokemonData[2:-1]
			pokemonData = pokemonData.split('], ')
			pokeList = {}
			for pokemon in pokemonData:
				pokemon = pokemon[1:]
				splitPokeData = pokemon.split("': [")
				pokemonName = splitPokeData[0]
				pokemonStats = [int(splitPokeData[1].split(', ')[0]), int(splitPokeData[1].split(', ')[1]), int(splitPokeData[1].split(', ')[2])]
				pokeList[pokemonName] = pokemonStats
			playerStats = splitPlayerData[1][2:-2]
			playerStats = playerStats.split(", '")
			candies = int(playerStats[0])
			currentPokemon = playerStats[1]
		
			gameData[playerName] = [pokeList, candies, currentPokemon]

gameData = {}
try:
	openGameSave('r+')
	currPlayer = changePlayer()
	gameOperationMode = 0
except:
	try:
		openGameSave('x+')
	except:
		print('The world is actually ending and I have failed as a programmer')
	gameOperationMode = -2
	currPlayer = ''

# GAME OPERATION MODES:
# -2 = Game starting over
# -1 = Stop the game
#  0 = Continue with the game
#  1 = Change player
#  2 = Changing profiles

while gameOperationMode != -1:
	print(gameData)
	if gameOperationMode == -2:
		addNewPlayer(input('What would you like your player\'s name to be? '))
		currPlayer = list(gameData.keys())[0]
		gameOperationMode = 0
	elif gameOperationMode == -1:
		saveGame()
	elif gameOperationMode == 0:
		gameOperationMode = printPlayerMenu(currPlayer)
	elif gameOperationMode == 1 or gameOperationMode == 2:
		currPlayer = changePlayer()
		gameOperationMode = printPlayerMenu(currPlayer)
	else:
		gameOperationMode = printPlayerMenu(currPlayer)
	

# If gameData file doesn't exist, start a new game without telling user and whatnot
# Use try block to handle fileNotFound exception or something like that 
# Fic printing of pokemon in catchNewPokemon
# intUserInput(question, min, max) 
# saveGame()