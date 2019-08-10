# Program to get mark of students, Store in dictionary
noOfStudents = int(input('Enter number of students - '))
dictionaryData = {}
for i in range(0, noOfStudents):
    rollNo = int(input('Enter Roll Number of Student {} - '.format(i+1)))
    name = str(input('Enter name of Student {} - '.format(i+1)))
    mark = float(input('Enter Mark of Student {} - '.format(i+1)))
    dictionaryData[i] = [rollNo, name, mark]
    print('')

print('---------  Python Mark List  ---------')
print('\tRoll No\t\tNAME\t\tMARK')
for j in range(0, noOfStudents):
    currentRow = dictionaryData.get(j)
    print('\t{0}\t\t\t{1}\t\t\t{2}'.format(currentRow[0], currentRow[1], currentRow[2]))

print('--------------------------------------')
