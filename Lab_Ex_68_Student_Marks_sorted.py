# Program to get mark of students, Store in dictionary, Sort
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
for i in range(0, noOfStudents):
    currentRow = dictionaryData.get(i)
    print('\t{0}\t\t\t{1}\t\t\t{2}'.format(currentRow[0], currentRow[1], currentRow[2]))

print('--------------------------------------')

# Sorting
for i in range(0, noOfStudents):
    for j in range(0, noOfStudents - i - 1):
        if dictionaryData.get(j)[2] < dictionaryData.get(j + 1)[2]:
            temp = dictionaryData[j]
            dictionaryData[j] = dictionaryData[j+1]
            dictionaryData[j] = temp

# Printing with rank (Sorted)
print('\n\n\t\t\tMark List With Rank')
print('---------  Python Mark List  ---------')
print('\tRoll No\t\tNAME\t\tMARK\t\tRANK')
for i in range(0, noOfStudents):
    currentRow = dictionaryData.get(i)
    print('\t{0}\t\t\t{1}\t\t\t{2}\t\t{3}'.format(currentRow[0], currentRow[1], currentRow[2], i+1))

print('--------------------------------------')
