# Program to square an entered number using Lambda/Anonymous functions
number = int(input('Enter a number to square - '))
square = lambda value: number ** 2
print("Square of {0} is {1}".format(number, square(number)))
