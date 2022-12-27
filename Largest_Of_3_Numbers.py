# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:58:33 2022

@author: amrit
"""

#1. Program to find biggest of three numbers while accepting input from user.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a > b and a > c:
    print(f"{a} is greater than {b} and {c}")
elif b > c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")