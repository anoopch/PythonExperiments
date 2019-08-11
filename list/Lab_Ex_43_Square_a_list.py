# Program to square an entered List

nos = int(input('Enter size of input Array - '))

myList = []
mySquaredList = []

for i in range(1, nos+1):
    temp = int(input('Enter number {0}:'.format(i)))
    myList.append(temp)
    mySquaredList.append(temp**2)

print('Entered Array - ', myList)
print('Squared Array - ', mySquaredList)