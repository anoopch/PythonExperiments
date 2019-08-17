from module import Lab_Ex_96_LCM_GCD_HCF as Math

num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the Second number: "))

print("The Highest Common Factor(HCF) of ({0}, {1}) is {2}.".format(num1, num2, Math.hcf(num1, num2)))

print("The Least Common Multiple(LCM) of ({0}, {1}) is {2}.".format(num1, num2, Math.find_lcm(num1, num2)))

print("The Greatest Common Divisor(GCD) of ({0}, {1}) is {2}.".format(num1, num2, Math.gcd(num1, num2)))
