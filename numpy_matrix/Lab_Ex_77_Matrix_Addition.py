# Read two matrices and perform addition
from numpy_matrix import Module_Matrix_Input as MatBox
import numpy

print('First Matrix')
matrix1 = MatBox.read_integer_matrix()
print('Second Matrix')
matrix2 = MatBox.read_integer_matrix()

if MatBox.is_addition_possible(matrix1, matrix2):
    print(numpy.add(matrix2, matrix1))
else:
    print('Unable to add matrices since sizes are different')
