# Program to find sum of natural numbers until the entered number using recursive functions
def natural_sum(num):
    if num > 1:
        return num + natural_sum(num - 1)
    else:
        return 1


number = int(input('Enter a the last number - '))
print("The sum of numbers from 1 to {0} is {1}".format(number, natural_sum(number)))
