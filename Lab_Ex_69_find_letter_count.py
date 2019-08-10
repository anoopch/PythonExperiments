# Program to count each character repeating in MISSISSIPPI
value = 'MISSISSIPPI'
# Find all unique letters
# find the counts
dictionary = {}
for i in range(0, len(value)):
    dictionary[value[i]] = value.count(value[i])

print(dictionary)
