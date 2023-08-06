#!/usr/bin/env python

"""
Author: saornek
Date: 2022
Last Updated: 08/03/2023
Purpose: Created for IC4U3 - Mecanum motor control with Adafruit TB6612
Notes: 
Code was mainly written for voice command control.
Mecanum Movements Inspired by https://www.researchgate.net/profile/Jin-Gang-Jiang-2/publication/307868549/figure/fig2/AS:713745810599936@1547181670156/Fig-5-Top-view-of-turning-principle-of-Mecanum-wheel.png
"""

from TB6612Library.py import *
import MecanumLib as ic4uMotors

while True:
    inputCommand = input("Command? ")
    if inputCommand == "s":
        ic4uMotors.robotMovements.stop()
    else:
        inputS = int(input("Speed?(0-100) "))
        if inputCommand == "f":
            ic4uMotors.robotMovements.forward(inputS)
        elif inputCommand == "b":
            ic4uMotors.robotMovements.backward(inputS)
        elif inputCommand == "s":
            ic4uMotors.robotMovements.stop()
        elif inputCommand == "cl":
            ic4uMotors.robotMovements.crabLeft(inputS)
        elif inputCommand == "cr":
            ic4uMotors.robotMovements.crabRight(inputS)
        elif inputCommand == "fl":
            ic4uMotors.robotMovements.fullTurnLeft(inputS)
        elif inputCommand == "fr":
            ic4uMotors.robotMovements.fullTurnRight(inputS)
