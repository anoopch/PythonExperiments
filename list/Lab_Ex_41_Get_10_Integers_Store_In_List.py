# Program to store 10 numbers in List by getting input from users
myList = []
for i in range(1, 11):
    temp = int(input('Enter number {0}:'.format(i)))
    myList.append(temp)

print('Entered List is - {0}'.format(myList))
