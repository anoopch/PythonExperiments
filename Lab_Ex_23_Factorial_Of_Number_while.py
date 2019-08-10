# Program to Factorial of a number
number = int(input('Enter an Integer number : '))
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0 or number == 1:
    print("The factorial of {0} is {1}".format(number, number))
else:
    i = 1
    factorial = 1
    while i < number + 1:
        factorial = factorial * i
        i += 1
    # for i in range(1, number + 1):
    # factorial = factorial * i
    print("The factorial of {0}, is {1}".format(number, factorial))
