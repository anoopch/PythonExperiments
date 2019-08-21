# Read two matrices and perform Multiply them
from numpy_matrix import Module_Matrix_Input as MatBox
import numpy

print('First Matrix')
matrix1 = MatBox.read_integer_matrix()
print('Second Matrix')
matrix2 = MatBox.read_integer_matrix()

if MatBox.is_multiplication_possible(matrix1, matrix2):
    print(numpy.dot(matrix2, matrix1))
else:
    print('Sorry !! Unable to multiply matrices since sizes are not matching M X N and N X M')
