# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:09:50 2022

@author: amrit
"""

#4. Write a program to convert Celcius to Fahrenheit or Fahrenheit to Celsius

"""
Forumula for celcius to fahrenheit 

F = (C *  (9/5)) + 32

Forumula for fahrenheit to celcius 

C = (5/9) *(F - 32)

"""

char1 = input("Type C for conversion from Celsius to Fahrenheit. Type F for conversion from Fahrenheit to Celcius.\n")
char = char1.lower()

if char == 'c':
    degrees = float(input("Enter the degrees in Celsius: "))
    fahrenheit = (degrees * (9/5)) + 32
    print(f"{degrees} in celsius is equal to {fahrenheit} in fahrenheit")
elif char == 'f':
    degrees = float(input("Enter the degrees in Fahrenheit: "))
    celsius = (5/9) *(degrees - 32)
    print(f"{degrees} in fahrenheit is equal to {celsius} in celsius")
else:
    print("Invalid")
    