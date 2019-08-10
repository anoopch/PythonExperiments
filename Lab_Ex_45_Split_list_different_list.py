# Program to split List by data type
originalList = [10, "Anoop CH", 12345.5677, "God", "BTEch", 12, 12.44, 10, 1, 3, 15]

integerList = []
stringList = []
floatList = []

for i in range(0, len(originalList)):
    if type(originalList[i]) == type('string'):
        stringList.append(originalList[i])
    elif type(originalList[i]) == type(1):
        integerList.append(originalList[i])
    elif type(originalList[i]) == type(1.0):
        floatList.append(originalList[i])
    else:
        print('Invalid Entry')

print('Integer List - ', integerList)
print('String List - ', stringList)
print('Float/Double List - ', floatList)
