# Program to generate a Random number within range
import random


def get_random_number(min_number, max_number):
    """
    This function takes a max number and returns a random number between min_number and max_number
    :max_number:  the max value of the random number
    :min_number:  the min value of the random number
    :return: a random number between min_number and max_number
"""

    return random.randint(min_number, max_number)


print(get_random_number(int(input('Enter min range - ')), int(input('Enter max range - '))))
