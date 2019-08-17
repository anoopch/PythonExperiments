# A Simple Calculator
def add(num1, num2):
    """
    This function takes two numbers as input and returns their sum
    :param num1: the first number
    :param num2: the second number
    :return: the sum of first and second number
    """
    return num1 + num2


def diff(num1, num2):
    """
    This function takes two numbers as input and returns their difference
    :param num1: the first number
    :param num2: the second number
    :return: the difference of first and second number
    """
    return num1 - num2


def division(num1, num2):
    """
    This function takes two numbers as input and returns the answer of first number divided by the second
    :param num1: the first number
    :param num2: the second number
    :return: the value of first number divided by the second number
    """
    return num1 / num2


def multiply(num1, num2):
    """
    This function takes two numbers as input and returns the answer of first number multiplied by the second
    :param num1: the first number
    :param num2: the second number
    :return: the value of first number multiplied by the second number
    """
    return num1 * num2


def mod(num1, num2):
    """
    This function takes two numbers as input and returns the balance after perfectly dividing first number by the second
    :param num1: the first number
    :param num2: the second number
    :return: the balance after perfectly dividing first number by the second
    """
    return num1 % num2


print('-------------------- CALCULATOR MENU --------------------\n\n',

      '\t\t1 - Add',
      '\n\t\t2 - Subtract',
      '\n\t\t3 - Multiply',
      '\n\t\t4 - Divide',
      '\n\t\t5 - Modulo',

      '\n-----------------------------------------------------')
choice = int(input('Enter Your menu Choice - '))
number01 = int(input('Enter the First Number - '))
number02 = int(input('Enter the Second Number - '))
value = 0

if choice == 1:
    value = add(number01, number02)
if choice == 2:
    value = diff(number01, number02)
if choice == 3:
    value = multiply(number01, number02)
if choice == 4:
    value = division(number01, number02)
if choice == 4:
    value = mod(number01, number02)
else:
    print('Invalid menu choice')

print('Result = ', value)
