# Program to find sum of all numbers in a set and print it
text = '8330844890240113'

# Finding letter counts
setData = set(text)

total = 0
for x in setData:
    total += int(x)

print('- Set -\n{0}\n{1}'.format(setData, total))
