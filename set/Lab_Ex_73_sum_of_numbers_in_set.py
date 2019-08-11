# Program to find sum of all numbers in a set and print it
text = '8330844890240113'

# Finding numbers and add to text - only uniques
setData = set(text)

#  Finding the total with iteration also sum() function is available
total = 0
for x in setData:
    total += int(x)

print('- Set -\n{0}\nSum = {1}'.format(setData, total))
