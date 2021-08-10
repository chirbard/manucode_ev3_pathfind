outputFile = open('output.py','w')
outputFile.write('''#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
wheel_diameter = 56
axle_track = 105
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

''')



inputFile = open('input.txt','r')
lines = inputFile.readlines()

# start pos = [2, 2] ; facing east/x+
currentPos = [2, 2, 'e']

def getXFromFile(line):
    if line[1] == ',':
        return int(line[0])
    return int(line[:2])

def getYFromFile(line):
    if line[-2] == ' ':
        return int(line[-1:])
    return int(line[-2:])

class changeDirection():
    def toEast(currentDirection):
        switch = {
            'w': 180,
            'n': 90,
            's': -90
        } 
        return switch.get(currentDirection, 'invalid direction')
    def toWest(currentDirection):
        switch = {
            'e': 180,
            'n': 90,
            's': -90
        } 
        return switch.get(currentDirection, 'invalid direction')
    def toSouth(currentDirection):
        switch = {
            'w': 90,
            'n': 180,
            'e': -90
        } 
        return switch.get(currentDirection, 'invalid direction')
    def toNorth(currentDirection):
        switch = {
            'w': -90,
            'e': 90,
            's': 180
        } 
        return switch.get(currentDirection, 'invalid direction')
    


def checkMovement(newPos, currentPos):
    if newPos[0] > currentPos[0]:
        # to e
        if currentPos[2] != 'e': outputFile.write('robot.turn({i})\n'.format(i = changeDirection.toEast(currentPos[2])))
        outputFile.write('robot.straight({i})\n'.format(i = (newPos[0] - currentPos[0]) * 100))
        return 'e'
    if newPos[0] < currentPos[0]:
        # to w
        if currentPos[2] != 'w': outputFile.write('robot.turn({i})\n'.format(i = changeDirection.toWest(currentPos[2])))
        outputFile.write('robot.straight({i})\n'.format(i = (currentPos[0] - newPos[0]) * 100))
        return 'w'
    if newPos[1] > currentPos[1]:
        # to s
        if currentPos[2] != 's': outputFile.write('robot.turn({i})\n'.format(i = changeDirection.toSouth(currentPos[2])))
        outputFile.write('robot.straight({i})\n'.format(i = (newPos[1] - currentPos[1]) * 100))
        return 's'
    if newPos[1] < currentPos[1]:
        # to n
        if currentPos[2] != 'n': outputFile.write('robot.turn({i})\n'.format(i = changeDirection.toNorth(currentPos[2])))
        outputFile.write('robot.straight({i})\n'.format(i = (currentPos[1] - newPos[1]) * 100))
        return 'n'



for line in lines:
    line = line.rstrip()
    if line == 'grip':
        outputFile.write('# grip\n')
    elif line == 'ungrip':
        # pärast ungrip peab liikuma 1 tagasi
        outputFile.write('# ungrip\n')
        outputFile.write('robot.straight(-100)\n')
        if currentPos[2] == 'e': currentPos[0] -= 1
        if currentPos[2] == 'w': currentPos[0] += 1
        if currentPos[2] == 'n': currentPos[1] += 1
        if currentPos[2] == 's': currentPos[1] -= 1
    else:
        newPos = [getXFromFile(line), getYFromFile(line)]
        # print(newPos) # for debug
        currentPos[2] = checkMovement(newPos, currentPos)

        currentPos[:2] = newPos[:2]
        # print(currentPos) # for debug
    

inputFile.close()
outputFile.close()
