# Program to print factors of an entered number
def print_factors(num):
    """
    This function takes a number and prints it's factors
    :param num: the number for which factors are to be found
    :return: No return, prints the result
    """

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


number = int(input('Enter a number to find the factors - '))

print(" Factors of "+str(number)+" are as follows")
print_factors(number)
