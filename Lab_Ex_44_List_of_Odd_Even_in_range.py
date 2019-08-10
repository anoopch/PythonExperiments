# Program to split List by odd and even
oddList = []
evenList = []

for i in range(1, 51):
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

print('Odd List - ', oddList)
print('Even List - ', evenList)
