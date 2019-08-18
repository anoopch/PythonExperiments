# Read two matrices and perform Subtraction
from numpy_matrix import Module_Matrix_Input as MatBox
import numpy

print('First Matrix')
matrix1 = MatBox.read_integer_matrix()
print('Second Matrix')
matrix2 = MatBox.read_integer_matrix()

if MatBox.is_subtraction_possible(matrix1, matrix2):
    print(numpy.subtract(matrix2, matrix1))
else:
    print('Unable to subtract matrices since sizes are different')
