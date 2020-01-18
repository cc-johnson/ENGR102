# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 4
# Date:        2 October 2019

cont = 'y'

while cont == 'y':
    col = int(input("How many columns would you like? ")) # User input for number of columns
    row = int(input("How may rows would you like? ")) # User input for number of rows

    numDash = (row * 5) # Roughly determine how many dashes to have on top and bottom

    print('-' * numDash)
    for i in range(1, row+1): # Print out the multiplication tables by row
        print("|  ", end="")
        for j in range(1, col+1): # Print out the correct value in that column within the row
            print(i*j, end="\t")
        print("|")
    print('-' * numDash)

    contIn = False
    while contIn != True:
        cont = input("Would you like to make another table (y/n)? ")
        cont = cont.lower()
        if cont == 'y' or cont == 'n':
            contIn = True
        else:
            print("Please type either 'y' or 'n'")
