# Program to find the HCF two numbers
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


num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
print("The Highest Common Factor(HCF)/"
      "Greatest Common Divisor(GCD) of ({0}, {1}) is {2}.".format(num1, num2,  hcf(num1, num2)))
