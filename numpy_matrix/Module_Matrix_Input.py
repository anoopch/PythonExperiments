# Module to read a matrix input in Row by Row fashion
def read_integer_matrix():
    matrix = []
    row_length = int(input('Enter no of Rows - '))
    col_length = int(input('Enter no of Columns - '))
    for i in range(row_length):
        temp_list = []
        print('Row {0}'.format(i + 1))
        for j in range(col_length):
            temp_list.append(int(input('Enter element {0} - '.format(j + 1))))
        matrix.append(temp_list)

    return matrix


def read_float_matrix():
    matrix = []
    row_length = int(input('Enter no of Rows - '))
    col_length = int(input('Enter no of Columns - '))
    for i in range(row_length):
        temp_list = []
        print('Row {0}'.format(i + 1))
        for j in range(col_length):
            temp_list.append(float(input('Enter element {0} - '.format(j + 1))))
        matrix.append(temp_list)

    return matrix


def read_complex_matrix():
    matrix = []
    row_length = int(input('Enter no of Rows - '))
    col_length = int(input('Enter no of Columns - '))
    for i in range(row_length):
        temp_list = []
        print('Row {0}'.format(i + 1))
        for j in range(col_length):
            temp_list.append(complex(input('Enter element {0} - '.format(j + 1))))
        matrix.append(temp_list)

    return matrix


def is_addition_possible(matrix1, matrix2):
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def is_subtraction_possible(matrix1, matrix2):
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def is_multiplication_possible(matrix1, matrix2):
    return matrix2.length == matrix1[0].length


def print_matrix(matrix):
    for i in range(matrix.length):
        print(matrix[i + 1])
