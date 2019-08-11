# Program to find if the entered number is divisible by another number
def division_checker(num, div):
    return num % div == 0


number = int(input('Enter the Number - '))
divider = int(input('Enter the Divider number - '))

if division_checker(number, divider):
    print('Number {0} is perfectly divisible by {1}'.format(number, divider))
else:
    print('Number {0} is NOT divisible by {1}'.format(number, divider))
