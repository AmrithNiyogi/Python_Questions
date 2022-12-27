# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:23:40 2022

@author: amrit
"""

import math as m

#5. Calculate area of a square and circle

def area_sqaure(side):
    area = side * side
    print(f"Area of square of side {side} = {area}")
    
def area_circle(radius):
    area = m.pi * pow(radius,2)
    print(f"Area of circle of radius {radius} = {area}")

isarea = True

while isarea:
    
    char1 = input("Enter S for calculating area of sqaure. Enter C for calculating area of circle.\n")
    char = char1.lower()
    
    if char == 's':
        side = float(input("Enter the length of side of a square: "))
        area_sqaure(side)
    elif char == 'c':
        radius = float(input("Enter the radius of the cirlce: "))
        area_circle(radius)
    else:
        print("Invalid Output")
        
    continue_area1 = input("Do you wish to find areas with different values. Type Y for yes, and N for no")
    continue_area = continue_area1.lower()
    
    if continue_area == 'y':
        isarea = True
    else:
        isarea = False
        