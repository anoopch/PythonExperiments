# Program to Shift a List circularly
originalList = [10, "Anoop CH", 12345.5677, "God", "BTEch", 12, 12.44, 10, 1, 3, 15]
print('Original List - ', originalList)

value = originalList.pop()

print('Popped - ', value)

originalList.insert(0, value)

print('Current List after rotation - ', originalList)
