# Program to check prime number
a=float(int(input('Enter an Integer : ')))
if((a==1) or (a==2) or (a==3) or (a==5) or (a==7)):
    print('Number entered {} is Prime'.format(a))
elif(((a%2)==0) or ((a%3)==0) or ((a%5)==0) or ((a%7)==0) ):
    print('Number entered {} is NOT Prime'.format(a))
else:
    print('Number entered {} is Prime'.format(a))
