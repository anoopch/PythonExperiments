print('Solving Quadratic Equation ax**2 + bx + c = 0\nIf any value is not in equation please enter 0\n')
a=int(input('Enter a : '))
b=int(input('Enter b : '))
c=int(input('Enter c : '))

discriminant=(b**2)-(4*a*c) 

x1=(-b -(discriminant**0.5))/(2*a)

x2=(-b +(discriminant**0.5))/(2*a)

print('The solutions of {}x**2 + {}x + {} = 0 are ({},{})'.format(a,b,c,x1,x2))
