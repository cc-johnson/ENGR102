# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones
# Section:     513
# Assignment:  Lab 13: Pokemon Project
# Date:        18 November 2019

from random import randint      # imported radint from random to use as an AI in rock, paper, scissor and generate candy
import csv                      # Imported csv to read the PokeList csv file given

# This is the best I can do. Tested it out and it worked fine but can probably be revised to make shorter or more
# efficient with the dictionaries.
def RPS():
    """Function to play rock paper scissors (RPS)"""
    print("Time to play rock, paper, scissors against Professor Oak!")
    print("Fight Professor Oak in a best of 3 match-up to win a new Pokemon and earn more candies.")
    print("1:\t Rock")
    print("2:\t Paper")
    print("3:\t Scissors")
    Player = int(input("Type in a number that corresponds to the weapon you want to choose: "))
    while Player < 1 or Player > 3:
        Player = int(input("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: "))
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
            Player = int(input("Type in a number that corresponds to the weapon you want to choose: "))
            while Player < 1 or Player > 3:
                Player = int(input("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: "))
            Oak = randint(1, 3)
            userWin += 1
            games += 1
        elif (Player == 3 and Oak == 1) or (Player == 1 and Oak == 2) or (Player == 2 and Oak == 3):
            print("Professor Oak wins this round!")
            print("1:\t Rock")
            print("2:\t Paper")
            print("3:\t Scissors")
            Player = int(input("Type in a number that corresponds to the weapon you want to choose: "))
            while Player < 1 or Player > 3:
                Player = int(input("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: "))
            Oak = randint(1, 3)
            userLoss += 1   # Used userLoss so game won't keep on going
            games += 1
        elif Player == Oak:
            print("It's a tie! Try again")
            print("1:\t Rock")
            print("2:\t Paper")
            print("3:\t Scissors")
            Player = int(input("Type in a number that corresponds to the weapon you want to choose: "))
            while Player < 1 or Player > 3:
                Player = int(input("Error! Please pick a number from 1-3 that corresponds to the weapon of choice: "))
            Oak = randint(1, 3)
    if userWin >= 2:
        print("Congratulations!! You have defeated Professor Oak in Rock, Paper, Scissor!!")
        return True
    elif userLoss >= 2:
        print("Sorry, Try again Later!!")
        return False
# May be a problem when fully testing the rock, paper, scissors game into the whole game overall


def catchNewPokemon():
    """Function to start a minigame to 'catch' a new pokemon. If player wins, award candies"""
    pokemon = []        # List to hold all pokemon
    user = RPS()        # RPS function use to determine if player will receive a pokemon and candies
    if user == True:
        with open('PokeList.csv', 'r') as file:     # for loop to only read the information and not the headers
            csvFile = csv.reader(file,delimiter=',')
            csvFile = [row for row in csvFile]
            csvFile = csvFile[1:]
            for row in csvFile:
                pokemon.append(row[1])
            userPick = []                   # List to only hold 5 random pokemon for player to choose
            randomSamp = randint(0, 148)    # Program chooses of number at random to determine the index to choose from
            for i in range(5):
                userPick.append(pokemon[randomSamp])
                randomSamp = randint(0, 148)
            print("Pick one pokemon from the 5 pokemon below by typing their corresponding number.")
            print("1:\t", userPick[0])
            print("2:\t", userPick[1])
            print("3:\t", userPick[2])
            print("4:\t", userPick[3])
            print("5:\t", userPick[4])
            pokeNum = int(input("Choose a pokemon from by typing the corresponding number from 1-5: "))
            while (pokeNum < 1) or (pokeNum > 5):
                pokeNum = int(input("Error, Make sure to type a number from 1-5 to pick a pokemon. "))
            if pokeNum == 1:
                newPoke = userPick[0]
            elif pokeNum == 2:
                newPoke = userPick[1]
            elif pokeNum == 3:
                newPoke = userPick[2]
            elif pokeNum == 4:
                newPoke = userPick[3]
            elif pokeNum == 5:
                newPoke = userPick[4]
            # random generator/ conditional statement to determine how many candies the player will receive
            RandomCandies = randint(0, 2)
            if RandomCandies == 0:
                RandomCandies = 3
            elif RandomCandies == 1:
                RandomCandies = 5
            elif RandomCandies == 2:
                RandomCandies = 10
            return(newPoke, RandomCandies)      # Not sure how to put them in the dictionary but these are the variables



# print(catchNewPokemon()) get rid of comments to test out everything
# print(RPS()) get rid of comment to only test RPS