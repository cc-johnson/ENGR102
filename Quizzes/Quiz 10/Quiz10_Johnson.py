# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 10
# Date:        20 November 2019

from random import uniform, randint

def checkSorted(numList):
    """Function to iterate through the list passed and determine if the list is completely sorted"""
    sorted = True
    for i in range(len(numList) - 1):
        # If the a number at i is not less than a number at i+1 in numList, stop the for loop and set sorted to False
        if not (numList[i] <= numList[i+1]):
            sorted = False
            break
    return sorted

def sortList(numList):
    """Function that picks two random numbers within the bounds of the passed list and if the number at ind2 is less
       than the number at ind1, then the list swaps the values"""
    ind1 = randint(0,len(numList)-1)
    ind2 = randint(0,len(numList)-1)
    if numList[ind2] < numList[ind1]:
        tmp = numList[ind1]
        numList[ind1] = numList[ind2]
        numList[ind2] = tmp
    return numList

# While loop to allow user to enter in the length of the list of numbers
# While loop is used to ensure the user is giving proper input as type integer
cont = False
while cont != True:
    try:
        howMany = int(input('How many numbers do you want to sort today? '))
        cont = True
    except:
        print("That's not an integer, please try again")

# List comprehension to generate n number of values, where n is the above user entered value
numList = [uniform(0,100) for i in range(howMany)]

# While loop is used to continue randomly sorting until the list is sorted
steps = 0 # Variable to count how many times the list was sorted
while checkSorted(numList) != True:
    sortList(numList)
    steps += 1

# Print out the result
print('List sorted in %d of steps!' % steps)
print('The sorted list is: ' + str(numList))