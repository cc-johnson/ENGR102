# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab06 Activity 2
# Date:        6 October, 2019

userInput = (input('Type in an integer (type q to quit): '))
numberList = []

while userInput != 'q':
    numberList.append(int(userInput))
    userInput = (input('Type in an integer (type q to quit): '))
evenNumList = []
for i in numberList:
    if i % 2 == 0:
        evenNumList.append(i)
for i in range(len(evenNumList)):
    for j in range(len(evenNumList)):
        if evenNumList[i] < evenNumList[j]:
            temp = evenNumList[j]
            evenNumList[j] = evenNumList[i]
            evenNumList[i] = temp
print(evenNumList)