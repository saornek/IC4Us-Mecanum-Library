#!/usr/bin/env python

"""
Author: saornek
Date: 08/04/2022
Last Updated: 08/06/2023
Purpose: Created for IC4U3 - Mecanum motor control with Adafruit TB6612.
Update: Added control test code below.
Notes: Mecanum Movements Inspired by https://www.researchgate.net/profile/Jin-Gang-Jiang-2/publication/307868549/figure/fig2/AS:713745810599936@1547181670156/Fig-5-Top-view-of-turning-principle-of-Mecanum-wheel.png
"""

import time
from TB6612Library import *

#Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
frontLeft = Motor(17,27,22,8,False)
frontRight = Motor(26,6,13,8,False)
backLeft = Motor(12,5,24,8,False)
backRight = Motor(11,10,9,8,False)

# You might want to change the code according to your hardware setup!!!

def stop():
    frontLeft.stop();
    backLeft.stop();
        
    frontRight.stop();
    backRight.stop();
        
def forward(speed):
    frontLeft.forward(speed);
    backLeft.forward(speed);
        
    frontRight.forward(speed);
    backRight.forward(speed);
        
def backward(speed):
    frontLeft.backward(speed);
    backLeft.backward(speed);
        
    frontRight.backward(speed);
    backRight.backward(speed);
        
def crabLeft(speed):
    frontLeft.backward(speed);
    backLeft.forward(speed);
        
    frontRight.forward(speed);
    backRight.backward(speed);
        
def crabRight(speed):
    frontLeft.forward(speed);
    backLeft.backward(speed);
        
    frontRight.backward(speed);
    backRight.forward(speed);
                
def fullTurnLeft(speed):
    frontLeft.backward(speed);
    backLeft.backward(speed);
        
    frontRight.forward(speed);
    backRight.forward(speed);
        
def fullTurnRight(speed):
    frontLeft.forward(speed);
    backLeft.forward(speed);
        
    frontRight.backward(speed);
    backRight.backward(speed);

while True:
    inputCommand = input("Command? ")
    if inputCommand == "s":
        stop()
    else:
        inputS = int(input("Speed?(0-100) "))
        if inputCommand == "f":
            forward(inputS)
        elif inputCommand == "b":
            backward(inputS)
        elif inputCommand == "cl":
            crabLeft(inputS)
        elif inputCommand == "cr":
            crabRight(inputS)
        elif inputCommand == "fl":
            fullTurnLeft(inputS)
        elif inputCommand == "fr":
            fullTurnRight(inputS)
