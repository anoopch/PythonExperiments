a=int(input('Enter first number : '))
b=int(input('Enter second number : '))

print('\nBefore swap :\nFirst number = {}\nSecond number = {}\n'.format(a,b));      
a=a+b;    
b=a-b;    
a=a-b;    
print('\nAfter swap :\nFirst number = {}\nSecond number = {}\n'.format(a,b));      
