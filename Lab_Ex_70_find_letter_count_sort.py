# Program to count each character repeating in MISSISSIPPI and sort by occurrences
text = 'MISSISSIPPI'
# Finding letter counts
dictionaryData = {}
for i in range(0, len(text)):
    dictionaryData[text[i]] = text.count(text[i])

print('Normal Dictionary', dictionaryData)

# getting the values inside dictionary
values = list(dictionaryData.values())
keyValues = list(dictionaryData.keys())
length = len(values)

# Sorting
for i in range(0, length):
    for j in range(0, length - i - 1):
        if int(values[j]) > int(values[j + 1]):
            temp = dictionaryData.get(keyValues[j])
            dictionaryData[keyValues[j]] = dictionaryData.get(keyValues[j + 1])
            dictionaryData[keyValues[j + 1]] = temp

print('Sorted Dictionary', dictionaryData)
