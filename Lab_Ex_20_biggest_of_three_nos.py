a=float(input('Enter first number : '))
b=float(input('Enter second number : '))
c=float(input('Enter third number : '))

if((a==b) and (b==c)):
    print('All numbers are equal')
elif((a>b)and(a>c)):
    print('First number {} is gratest'.format(a))
elif((b>a)and(b>c)):
    print('Second number {} is greatest'.format(b))
elif((c>a)and(c>b)):
    print('Third number {} is gratest'.format(c))
else:
    print('Some numbers are equal')
