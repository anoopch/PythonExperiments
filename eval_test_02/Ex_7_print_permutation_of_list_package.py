def read_integer_list():
    temp_list = []
    length = int(input('Enter no of elements in the list - '))
    for i in range(length):
        temp_list.append(int(input('Enter element {0} - '.format(i + 1))))

    return temp_list


def combinations(lst, length):
    """ Find all combinations of the specified length from a list. """
    if length == 0:
        return [[]]
    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]
        for p in combinations(remLst, length - 1):
            l.append([m] + p)
    return l


integer_list = read_integer_list()
print(combinations(integer_list, len(integer_list)))

# Not Working needs more work skipping
