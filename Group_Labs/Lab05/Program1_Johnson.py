# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 05 Activity 1 Program 1
# Date:        29 September, 2019

prevNum = 0
curNum = 1
sequence = "0 1 "
print("The current number in the sequence is", curNum)
userNum = int(input("What is the next number in the sequence? "))
while(userNum == prevNum + curNum):
	prevNum = curNum
	curNum = userNum
	sequence += str(userNum) + " "
	print("\nSequence entered:", sequence)
	print("The current number in the sequence is", curNum)
	userNum = int(input("What is the next number in the sequence? "))