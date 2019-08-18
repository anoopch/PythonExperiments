# Convert a list into a new unique
def get_unique_list(normal_list):
    return list(set(normal_list))


count = int(input('Enter number of elements in list - '))
m_list = []
for i in range(1, count + 1):
    m_list.append(int(input('Enter number {0} in the list - '.format(i))))

print('Entered list - ', m_list)
print('Unique list - ', get_unique_list(m_list))
