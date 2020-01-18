# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Anna Olmedo, Chase Johnson, Bryan Jones
# Section:     413
# Assignment:  Lab Assignment 4, Activity 2
# Date:        16 September 2019

# __init__
firstStop = 0.3
secondGo = 0.4
increment = 0.1

# start
currentAlt = float(input('Current Altitude: '))

# initial method of comparing to direct values
if currentAlt == 0.3:
    print('Stop the first stage!')  
elif currentAlt == 0.4:
    print('Start the second stage!')
else:
    print('No action required at this point')

# final method, using tolerances
tol = 1 * (10 ** -8)
if abs(currentAlt - 0.3) < tol:
    print('Stop the first stage!')
elif abs(currentAlt - 0.4) < tol:
    print('Start the second stage!')
else:
    print('No action required at this point')
    # Testing vars and such ---> Ignore
        # tf3 = tf4 = False
        # if abs(currentAlt - 0.3) < tol:
        #     tf3 = True
        # if abs(currentAlt - 0.4) < tol:
        #     tf4 = True
        # print("tol: " + str(tol))
        # print("currentAlt - 0.3: " + str(abs(currentAlt-0.3)), "and is less than tol", tf3)
        # print("currentAlt - 0.4: " + str(abs(currentAlt-0.4)), "and is less than tol", tf4)


