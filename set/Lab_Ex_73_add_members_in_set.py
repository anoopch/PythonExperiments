# Program to find sum of all numbers in a set and print it
text1 = '8330844890240113'

# Finding numbers and add to set - only uniques
setData = set(text1)
print('- Initial Set -\n{0}'.format(setData))

# Finding numbers and add to set - only uniques, add one-by-one to the set
text2 = set('912132130012')
for x in text2:
    setData.add(x)
print('- Second Set -\n{0}'.format(setData))

# Simple=y adding a random number
setData.add(10)
print('- Third Set -\n{0}'.format(setData))
