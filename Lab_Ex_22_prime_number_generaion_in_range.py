# Program to print prime numbers in a range
start=int(input('Enter starting range : '))
end=int(input('Enter ending range : '))

a=start;
print('Prime numbers between {} and {}'.format(start,end))

while(a<=end):
    if((a==1) or (a==2) or (a==3) or (a==5) or (a==7)):
        print(a)
    elif(((a%2)!=0) and ((a%3)!=0) and ((a%5)!=0) and ((a%7)!=0) ):
        print(a)
    a+=1
print('End')
