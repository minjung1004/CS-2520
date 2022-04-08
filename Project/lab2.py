#Name: Min Jung
#Due Date: October 31, 2021
#Project 1: Lab 2

import math 
from sys import exit

tries = 0
while True:
    try:
        x0 = int(input("Enter value for x0:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()

while True:
    try:
        y0 = int(input("Enter value for y0:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()
while True:
    try:
        x1 = int(input("Enter value for x1:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()

while True:
    try:
        y1 = int(input("Enter value for y1:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()

while True:
    try:
        r0 = int(input("Enter value for r0:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()
            
while True:
    try:
        r1 = int(input("Enter value for r1:"))
        break
    except ValueError:
        print("\nNot a int value. Try again.")
        tries += 1
        if tries == 3:
            print("Thrid attempt. Exiting program.")
            exit()


d = math.sqrt((x1-x0)**2 + (y1-y0)**2)


if d > r0+r1:
    print("the two circles do not intersect and are separate.")
elif d < abs(r0-r1):
    print("the two circles do not intersect, and one is contained within the other.")
elif d == r0+r1:
    print("the two circles intersect a single point.")
elif d == 0 and r0 == r1:
    print("the two circles are coincident.")
else:
    print("the two circles intersect at two points.")

