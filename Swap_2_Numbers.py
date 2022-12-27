# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:02:19 2022

@author: amrit
"""

#2. Program to accept two numbers and swap them

a = input("Enter the first number: ")
b = input("Enter the second number: ")

print("Before SWAP\n")
print(f"Vale of a = {a} and b = {b}")

temp = a
a = b
b = temp

print("After SWAP\n")
print(f"Vale of a = {a} and b = {b}")