#Name: Patrick Martinez
#Date: 11/14/2017
#Program: LHS & RHS Calculations
#Purpose: Used for lab 9 to calculate LHS and RHS for torque lab.

import math

#Constants
WEIGHT_MASS = 212

#Variables
m1   = int(input("enter m1: "))
m2   = int(input("enter m2: "))
m3   = int(input("enter m3: "))
                                #Convert to m
r1 = int(input("enter r1(in cm): ")) * .01
r2 = int(input("enter r2(in cm): ")) * .01
r3 = int(input("enter r3(in cm): ")) * .01

theta = (float(input("enter degrees: "))) * (math.pi/180)

#Calcluations
LHS = ((r1 * math.cos(theta) * m1) + 
      ((.866) * r3 * math.sin(theta) * m3))

RHS = (((.5) * r2 * math.cos(theta) * m2) + 
      ((.5) * r3 * math.cos(theta) * m3) + 
      ((.866) * r2 * math.sin(theta) * m2))

PercentDifference = (LHS - RHS)/LHS

print ("LHS: " + format(LHS))
print ("RHS: " + format(RHS))
print ("%Diff: " + format(PercentDifference))
