def row_swap(matrix_swaped, row_1, row_2):
    row_1_data = matrix_swaped[row_1]
    row_2_data = matrix_swaped[row_2]
    matrix_swaped[row_1] = row_2_data
    matrix_swaped[row_2] = row_1_data

    return matrix_swaped

def row_add(matrix_added, row_1, row_2, multiplier):
    row_1_data = matrix_added[row_1]
    row_2_data = matrix_added[row_2]
    multiplied_row_2 = [element*multiplier for element in row_2_data]
    new_row_1 = []
    for index, element in enumerate(row_1_data):
        new_row_1.append(element + multiplied_row_2[index])
    matrix_added[row_1] = new_row_1

    return(matrix_added)

def row_multiply(matrix_multiplied, row, multiplier):
    multiplied_row = [element*multiplier for element in matrix_multiplied[row]]
    matrix_multiplied[row] = multiplied_row

    return(matrix_multiplied)

def leading_1_candidate(matrix1, column):
    for index,row in enumerate(matrix1[(column-1):]):
        if row[column-1]!=0:
            return [index, row[column-1]]


def create_leading_1(matrix1, column):
    if leading_1_candidate(matrix1, column) != None:
        row = leading_1_candidate(matrix1, column)[0] + column-1
            
        #+1
        leading = leading_1_candidate(matrix1, column)[1]
        new_matrix = row_multiply(matrix1, row, (1/leading))
        new_matrix = row_swap(new_matrix, row, column-1)
        for index,element in enumerate(new_matrix):
            if element[column-1]!=0 and index> column-1:
                new_matrix = row_add(new_matrix, index, column-1, -element[column-1])
    else:
        return matrix1
    return new_matrix

def row_reduction(matrix, j=0):
    n = len(matrix[0])
    if j == int(n):
        return(matrix)
    else:
        return(row_reduction(create_leading_1(matrix,j+1), j+1))
