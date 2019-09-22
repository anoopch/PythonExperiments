from itertools import permutations


def read_integer_list():
    temp_list = []
    length = int(input('Enter no of elements in the list - '))
    for i in range(length):
        temp_list.append(int(input('Enter element {0} - '.format(i + 1))))

    return temp_list


integer_list = read_integer_list()
result = permutations(integer_list)
gen = 0
for val in result:
    print(val)
    gen += 1
print('\n\nTotal permutations {0} generated\n\n', gen)
