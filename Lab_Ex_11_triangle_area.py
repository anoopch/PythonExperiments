a=float(input('Enter first side of triangle : '))
b=float(input('Enter second side of triangle : '))
c=float(input('Enter third side of triangle : '))

s=(a+b+c)/2
area=((s-a)*(s-b)*(s-c))**0.5

print('Side 1\t:\t{}\nSide 2\t:\t{}\nSide 3\t:\t{}\nArea of triangle\t:\t{}'.format(a,b,c,area))
