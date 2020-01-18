# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Quiz 7
# Date:        30 October 2019

# Dataset used for testing purposes: [40.56, 85.945],[40.75, 87.112],[38.15,96.097]
sensor_data = [[40.56, 85.945],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097],[40.75, 87.112],[38.15,96.097]]

# Line 15 opens the log file under an object named $file
# I use x+ assuming that the file does not already exist, if the file already exists, r+ would be more appropriate
with open('refineryInletLog.txt', 'r+') as file:
    # The following lines write the information about the factory and the day the log was created
    file.write('Oil Company Refinery\n')
    file.write('Log Date: Oct. 30, 2019\n')
    file.write('------------------------------\n')
    # The following lines set up the table for the data to be added
    file.write('Time   Avg Temp   Avg Flowrate\n')
    file.write('(hr)        (C)          (gpm)\n')
    hourCount = 1
    for hour in sensor_data:
        # The following lines handle writing the data in $sensor_data to the log file
        file.write('  %02s      %2.2f         %2.3f\n' % (hourCount, hour[0], hour[1]))
        hourCount += 1

