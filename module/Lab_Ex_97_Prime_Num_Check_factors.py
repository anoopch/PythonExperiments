# Module to check if a number is prime
def check_prime(number):
    """This function takes an integer input

    :param number: The number to be checked if it's prime
    :return:
        True if it is a Prime number
        False if it is not a Prime Number
    """

    if (number == 1) or (number == 2) or (number == 3) or (number == 5) or (number == 7):
        return True
    elif ((number % 2) == 0) or ((number % 3) == 0) or ((number % 5) == 0) or ((number % 7) == 0):
        return False
    else:
        return True


def get_factors(num):
    """
    This function takes a number and prints it's factors
    :param num: the number for which factors are to be found
    :return: the list of factors for the given number
    """
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors
