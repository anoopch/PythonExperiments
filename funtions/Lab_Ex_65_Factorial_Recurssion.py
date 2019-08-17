# Program to find factorial of an entered number using recursive functions
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


number = int(input('Enter a number - '))
print("Factorial of {0} is {1}".format(number, factorial(number)))
