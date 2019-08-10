# Program to change the contents of a list containing Tuples
myTuplesList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
newDataToUpdate = (100, 100, 100)
newList = []
for i in range(0, len(myTuplesList)):
    tempList = list(myTuplesList[i])
    tempList[len(tempList) - 1] = 100
    newList.append(tuple(tempList))

print('Original List of Tuples - ', myTuplesList)
myTuplesList = newList
newList = []
print('Modified List of Tuples - ', myTuplesList)
