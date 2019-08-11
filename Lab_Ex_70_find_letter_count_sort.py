# Program to count each character repeating in MISSISSIPPI and sort by occurrences
text = 'MISSISSIPPI'
# Finding letter counts
dictionaryData = {}
for i in range(0, len(text)):
    dictionaryData[text[i]] = text.count(text[i])

print('- Dictionary with letter count -\n', dictionaryData)

# getting the values inside dictionary
values = list(dictionaryData.values())
keyValues = list(dictionaryData.keys())
length = len(values)

# Sorting
temp = []
for i in range(0, length):
    for j in range(0, length - i - 1):
        if int(values[j]) > int(values[j + 1]):
            temp = keyValues[j]
            keyValues[j] = keyValues[j + 1]
            keyValues[j + 1] = temp

            temp = values[j]
            values[j] = values[j + 1]
            values[j + 1] = temp

# Create a new Dictionary
newDictionary = {}
for i in range(0, length):
    newDictionary[keyValues[i]] = values[i]

print('- Sorted Dictionary -\n', newDictionary)
