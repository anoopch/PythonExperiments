# Program to count each character repeating in MISSISSIPPI
value = 'MISSISSIPPI'

dictionary = {}
for i in range(0, len(value)):
    dictionary[value[i]] = value.count(value[i])

print(dictionary)
