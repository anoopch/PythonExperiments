# Program to Factorial of a number - using while
number = int(input('Enter an Integer number : '))

for i in range(1, 16):
    print("{0} X {1} = {2}".format(i, number, number*i))
