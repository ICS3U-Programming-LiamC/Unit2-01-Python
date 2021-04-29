#!/usr/bin/env python3
# Created By: Liam Csiffary
# Date: April 28, 2021
# this code solves for the area and perimeter of a circle
# using math.pi and not 3.14


import math


# creates function to run
def main():
    # asks user for inputs
    rad_str = input("Radius = ")
    unit = input("The unit you're useing is = ")
    precision_str = input("Number of decimal places = ")
    # turns the inputs from strings into integers
    rad = int(rad_str)
    precision = int(precision_str)

    # calculates the area and perimeter
    area = math.pi*rad**2
    perimeter = math.pi*rad*2

    area_rounded = "{:.{}f}".format(area, precision)
    perimeter_rounded = "{:.{}f}".format(perimeter, precision)

    print("The area of a circle with a radius of {}{} is {}{}^2\
    ".format(rad, unit, area_rounded, unit))

    print("The perimeter of a circle with a radius of {}{} is {}{}\
    ".format(rad, unit, perimeter_rounded, unit))


if __name__ == "__main__":
    main()
