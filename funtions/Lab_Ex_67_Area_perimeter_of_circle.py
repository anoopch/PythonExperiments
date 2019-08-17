# Program to find the are and circumference of a circle
import math
radius = float(input('Enter the radius of circle - '))
area = lambda value: 2 * math.pi * radius
circumference = lambda value: math.pi * (radius ** 2)
print("Area of circle with radius {0} is {1}".format(radius, area(radius)))
print("Circumference of circle with radius {0} is {1}".format(radius, circumference(radius)))
