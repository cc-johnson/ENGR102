# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 9
# Date:        13 November 2019

"""Write a function that takes two parameters, a students name and list of grades (of unknown length), and returns the name and a letter grade.

Your function must find the average of the grades, and determine the letter grade (A >= 90, B >=80, C >=70, D >=60, F <60).
The student name comes in to the function as ‘First Last’. You should return it as ‘Last, First’. Assume all names include only
    one first name and one last name (that is, there is only one space found in the string).
Your main code must supply two test cases for the function, and print the output to the user.
"""

from random import uniform

def calcLetterGrade(stuName, grades):
    gradeAvg = sum(grades)/len(grades)
    if gradeAvg >= 90:
        letterGrade = 'A'
    elif gradeAvg >= 80:
        letterGrade = 'B'
    elif gradeAvg >= 70:
        letterGrade = 'C'
    elif gradeAvg >= 60:
        letterGrade = 'D'
    elif gradeAvg < 60:
        letterGrade = 'F'

    stuName = stuName.split(' ')
    stuName = stuName[1] + ', ' + stuName[0]

    print(stuName.split(', ')[1] + '\'s grades are: ' + str(grades))
    return stuName + ' has a grade average of: ' + letterGrade + '\n'

grades = [round(uniform(50,100), 2) for i in range(0,4)]
name = 'Markus Powell'
print(calcLetterGrade(name, grades))

grades = [round(uniform(50,100), 2) for i in range(0,6)]
name = 'Chelsea Wayward'
print(calcLetterGrade(name, grades))