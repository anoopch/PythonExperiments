# Module to generate a series
def get_series(num):
    """
    This function takes a number and prints it's factors
    :param num: the number for which factors are to be found
    :return: the list of factors for the given number
    """
    factors = []
    for i in range(1, num + 1):
        factors.append(i)

    return factors
