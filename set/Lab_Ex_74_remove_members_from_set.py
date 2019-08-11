# Program to find sum of all numbers in a set and print it
text1 = '8330844890240113'

# Finding numbers and add to set - only uniques
setData = set(text1)
print('- Initial Set -\n{0}'.format(setData))

numberToRemove = int(input('Enter a Number in the above set to remove - '))

if numberToRemove in setData:
    setData.remove(numberToRemove)
else:
    print('Sorry!! Entered number {0} is not found in the set.'.format(numberToRemove))

print('Result Set after operation\n', setData)
