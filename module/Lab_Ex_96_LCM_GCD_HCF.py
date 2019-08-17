def find_lcm(first_number, second_number):
    """This function takes two
    integers as input and returns
    the calculated Least Common Multiple(LCM)"""
    return (first_number * second_number) // hcf(first_number, second_number)


def hcf(first_number, second_number):
    """This function takes two
    integers as input and returns
    the calculated Highest Common Factor(HCF)/Greatest Common Divisor(GCD)"""
    result = 1
    if first_number > second_number:
        smaller = second_number
    else:
        smaller = first_number

    for i in range(1, smaller + 1):
        if first_number % i == 0 and second_number % i == 0:
            result = i
    return result


def gcd(first_number, second_number):
    """This function takes two
    integers as input and returns
    the calculated Highest Common Factor(HCF)/Greatest Common Divisor(GCD)"""
    result = 1
    if first_number > second_number:
        smaller = second_number
    else:
        smaller = first_number

    for i in range(1, smaller + 1):
        if first_number % i == 0 and second_number % i == 0:
            result = i
    return result

