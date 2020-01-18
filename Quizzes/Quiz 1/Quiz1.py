	from math import *

	# By submitting this assignment, I agree to the following:
	#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
	#  “I have not given or received any unauthorized aid on this assignment”
	#
	# Name:           Chase Johnson
	# Section:        413
	# Team:           23
	# Assignment:     Quiz 1
	# Date:           11 September, 2019

	# defines the radius of a sphere as 4 cm.
	radius = 4 #cm

	# calculates the volume of the sphere (Vsphere = 4/3*pi*r^3).
	volumeSphere = (4/3)*pi*(radius**3)

	# calculates how many complete times the sphere, if filled with liquid repetitively, 
	# could be emptied into a cube with a side length of 40 cm. Assume the sphere is 
	# perfectly filled, and perfectly emptied into the cube each time.
	side = 40 #cm
	volumeCube = side ** 3
	fillNum = volumeCube // volumeSphere

	# calculates what volume of  liquid is remaining in the sphere once the cube is filled.
	percentLeft = ((volumeCube / volumeSphere) - fillNum)
	volSphereLeft = percentLeft * volumeSphere

	# outputs a descriptive sentence informing the user of how many complete times the 
	# sphere was filled, and what volume of liquid remains in the sphere.
	print("The sphere can be emptied into the cube a total of", fillNum, "times.")
	print("The sphere will have", volSphereLeft, "cm3 remaining once the cube is filled.")

	# Debugging stuff
	# print("-----------------------------------------------------------------------------")
	# print("Other information:")
	# print("Volume of sphere: " + str(volumeSphere))
	# print("Volume of cube: " + str(volumeCube))
	# print("Percent of sphere volume left: " + str(percentLeft))