# Program to split List by data type
originalList = [10, "Anoop CH", 12345.5677, "God", "BTEch", 12, 12.44, 10, 1, 3, 15, (1, 2, 3)]

count = 0
for i in range(0, len(originalList)):
    if type(originalList[i]) == type((10, 12, 13)):
        print('Tuple found at index {0} - Stopping'.format(i))
        break
    else:
        count += 1

print('Total elements in List before finding a tuple - ', count)
