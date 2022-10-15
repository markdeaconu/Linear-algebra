from mcopy2 import mcopy
def del_element(matrix, m, n = 'row'):
    new_matrix = mcopy(matrix)
    if n == 'row':
        del new_matrix[m]
    else:
        del new_matrix[m][n]
    return new_matrix

def determinant_prep(matrix, k):
    new_matrix = []
    for row in range(len(matrix)):
        if new_matrix == []:
            new_matrix = del_element(matrix, row, k-1)
        else:
            new_matrix = del_element(new_matrix, row, k-1)
    new_matrix = del_element(new_matrix, 0)
    return new_matrix

def determinant(matrix):
    deter = 0
    if len(matrix) == 2 or len(matrix[0]) == 2:
        deter = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        for i in range(len(matrix[0])):
            deter += (matrix[0][i])* determinant(determinant_prep(matrix, i+1)) * ((-1)**(i))
    return deter
