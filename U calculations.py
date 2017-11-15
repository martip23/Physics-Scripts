#Name: Patrick Martinez
#Date: 11/14/2017
#Program: Potential Energy Calculations
#Purpose: Used for lab 9 to calculate Potential Energy

import math

#Constants
G = 9.8
WEIGHT_MASS = 212

#Variables
    #Masses                                 Convert to kg
m1   = int(input("enter m1: ")) * .001 * WEIGHT_MASS
m2   = int(input("enter m2: ")) * .001 * WEIGHT_MASS
m3   = int(input("enter m3: ")) * .001 * WEIGHT_MASS

    #Radii                          Convert to m
r1  = int(input("enter r1(in cm): ")) * .01
r2  = int(input("enter r2(in cm): ")) * .01
r3  = int(input("enter r3(in cm): ")) * .01

theta1   = (float(input("angleA(in degrees): ")))
theta2   = (float(input("angleB(in degrees): ")))

#Functions
    #Main loop
def main():
    UA  = potentialEnergy(theta1)
    UB  = potentialEnergy(theta2)
    print("Potential Energy of A: " + format(UA))
    print("Potential Energy of B: " + format(UB))

    #gets sin of an angle in degrees (converts to radians for math.sin)
def sine(angle):
    radians = (angle * (math.pi/180))
    return math.sin(radians)

    #calculates potential energy
def potentialEnergy(angle):
    return ((m1 * G * r1 * sine(angle)) +
            (m2 * G * r2 * sine(angle + 120)) +
            (m3 * G * r3 * sine(angle + 240)))

#Function Call
main()
