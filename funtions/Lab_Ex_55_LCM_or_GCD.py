# Program to find the LCM or GCD of two numbers
def find_lcm(first_number, second_number):
    """This function takes two
    integers as input and returns
    the calculated Least Common Multiple(LCM)/Greatest Common Divisor(GCD)"""
    if first_number > second_number:
        bigger = second_number
    else:
        bigger = first_number

    while True:
        if bigger % first_number == 0 and bigger % second_number == 0:
            return bigger
        bigger += 1


num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))
print("The Least Common Multiple(LCM)/"
      "Greatest Common Divisor(GCD) of ({0}, {1}) is {2}.".format(num1, num2, find_lcm(num1, num2)))
