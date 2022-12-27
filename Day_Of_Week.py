# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:33:11 2022

@author: amrit
"""

#6. Write a program to print the day of the week

days_week = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    }


def get_key(val):
    for key, value in days_week.items():
        if val == value:
            return key
 
    return "key doesn't exist"

day = int(input("Enter a number from 0 to 6: "))

print(get_key(day))
