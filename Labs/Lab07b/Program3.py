# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 07b Program 3
# Date:        13, October 2019
from collections import namedtuple

# Create a new named tuple to maintain the information about each class
course = namedtuple('Class', ['name','creditHours','letterGrade'])  # Create the named tuple

# Ask the user for the number of courses
numCourses = int(input("How many courses are you taking this semester? "))

# Store each of the named tuples in here
courses = []

# Get the details for each class
for i in range(numCourses):
	courseName = input("What is the name of class " + str(i+1) + "? ")
	courseHours = int(input("How many hours is " + courseName + " worth? "))
	courseGrade = input("What is the letter grade of class " +  courseName + "? ")

	courses.append(course(courseName, courseHours, courseGrade))

totGradePoints = 0.0
totCreditHours = 0
# Calculate the grade points and credit hours earned
for course in courses:
	courseGrade = course.letterGrade
	creditHours = course.creditHours
	totCreditHours += creditHours

	if courseGrade == 'a':
		totGradePoints += 4.0 * creditHours
	elif courseGrade == 'b':
		totGradePoints += 3.0 * creditHours
	elif courseGrade == 'c':
		totGradePoints += 2.0 * creditHours
	elif courseGrade == 'd':
		totGradePoints += 1.0 * creditHours

# Dump out the students GPA
print("Your GPA is a: " + str(round(totGradePoints/totCreditHours, 2)))