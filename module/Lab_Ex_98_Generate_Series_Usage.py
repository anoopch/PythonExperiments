# Program to generate a series using Modules

from module import Lab_Ex_98_Generate_Series as Module

number = int(input('Enter the last number - '))

print('The series ending {0} are as below\n{1}\n'.format(number, Module.get_series(number)))
