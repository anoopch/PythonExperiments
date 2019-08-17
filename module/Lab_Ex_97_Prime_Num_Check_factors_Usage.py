# Program to check entered number is prime number and generate its factors using Modules

from module import Lab_Ex_97_Prime_Num_Check_factors as Module

number = int(input('Enter a Number - '))
if Module.check_prime(number):
    print('Entered number {0} is prime'.format(number))
else:
    print('Entered number {0} is NOT prime'.format(number))

print('The factors of {0} are {1}'.format(number, Module.get_factors(number)))
