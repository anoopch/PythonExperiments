# Read two matrices and perform addition
from numpy_matrix import Module_Matrix_Input as MatBox
import numpy

print('Matrix')
matrix1 = MatBox.read_integer_matrix()

print(matrix1)
print(numpy.transpose(matrix1))
