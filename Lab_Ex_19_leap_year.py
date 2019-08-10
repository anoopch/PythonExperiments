# Program to check if a number ented is a leap year

year=int(input('Enter a positive Integer for Year : '))

if((year%400)==0):
    print('Entered year is Leap year!')
elif((year%100)==0):
    print('Entered year is NOT a Leap year!')
elif((year%4)==0):
    print('Entered year is Leap year!')
else:
    print('Entered year is NOT a Leap year!')
