#!/usr/bin/env python

"""
Author: saornek
Date: 2022
Last Updated: 08/03/2023
Status: needs to be tested
Purpose: Created for IC4U3 - Mecanum motor control with Adafruit TB6612
Notes: 
Code was mainly written for voice command control. It has been adapted to Tkinter GUI code in 2023 to be easily tested.
Mecanum Movements Inspired by https://www.researchgate.net/profile/Jin-Gang-Jiang-2/publication/307868549/figure/fig2/AS:713745810599936@1547181670156/Fig-5-Top-view-of-turning-principle-of-Mecanum-wheel.png
"""

# Import gui library
import tkinter as tk

#functions for testing purposes
def stop():
    print("Stop")

def forward():
    print("Forward")

def backward():
    print("Backward")

def crab_left():
    print("Left (Crab Mode)")

def crab_right():
    print("Right (Crab Mode)")

def fully_left():
    print("Left (Fully)")

def fully_right():
    print("Right (Fully)")

# Create the main GUI window
root = tk.Tk()
root.title("Mecanum Motor Control")

# Create buttons
btnStop = tk.Button(root, text="Stop", command=stop)
btnForward = tk.Button(root, text="Forward", command=forward)
btnBackward = tk.Button(root, text="Backward", command=backward)
btnCrabLeft = tk.Button(root, text="Left (Crab Mode)", command=crab_left)
btnCrabRight = tk.Button(root, text="Right (Crab Mode)", command=crab_right)
btnFullyLeft = tk.Button(root, text="Left (Fully)", command=fully_left)
btnFullyRight = tk.Button(root, text="Right (Fully)", command=fully_right)

# Create button grid
btnStop.grid(row=0, column=0, padx=10, pady=5)
btnForward.grid(row=0, column=1, padx=10, pady=5)
btnBackward.grid(row=0, column=2, padx=10, pady=5)
btnCrabLeft.grid(row=1, column=0, padx=10, pady=5)
btnCrabRight.grid(row=1, column=1, padx=10, pady=5)
btnFullyLeft.grid(row=1, column=2, padx=10, pady=5)
btnFullyRight.grid(row=2, column=1, padx=10, pady=5)

# Start the GUI
root.mainloop()
