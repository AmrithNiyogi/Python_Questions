# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:05:27 2022

@author: amrit
"""

#3. Accept a number from the user and print its multiplication table

number = int(input("Enter a number: "))
range_mult = int(input("Till which number do you wish to print multiplication tables: "))

for i in range(1,range_mult+1):
    a = number * i
    print(f"{number} * {i} = {a}")
