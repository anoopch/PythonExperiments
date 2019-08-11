# Program to store 10 numbers in List by getting input from users
myList = []
for i in range(1, 11):
    temp = int(input('Enter number {0}:'.format(i)))
    myList.append(temp)

searchValue = int(input('Enter a number to search - '))
if searchValue in myList:
    print('Entered number {0} is found in entered list'.format(searchValue))
else:
    print('Sorry!! Entered number {0} is NOT found in entered list'.format(searchValue))

print('Entered List is - {0}'.format(myList))
