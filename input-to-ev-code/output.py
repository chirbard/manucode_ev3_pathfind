#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track = 105
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

robot.straight(500)
robot.turn(90)
robot.straight(200)
# grip
robot.turn(180)
robot.straight(200)
robot.turn(90)
robot.straight(1400)
# ungrip
robot.straight(-100)
robot.turn(90)
robot.straight(600)
robot.turn(90)
robot.straight(500)
# grip
robot.turn(180)
robot.straight(500)
robot.turn(-90)
robot.straight(500)
# ungrip
robot.straight(-100)
robot.turn(-90)
robot.straight(500)
# grip
robot.turn(180)
robot.straight(300)
robot.turn(-90)
robot.straight(100)
# ungrip
robot.straight(-100)
robot.turn(-90)
robot.straight(1000)
robot.turn(-90)
robot.straight(500)
# grip
robot.turn(180)
robot.straight(700)
robot.turn(90)
robot.straight(700)
# ungrip
robot.straight(-100)

