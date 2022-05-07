from matrix import matrix as mtx

def determinant(matrix):
    if matrix.rows == 1:
        return matrix.matrix[0][0]
    if matrix.rows == 2:
        a, b = matrix.matrix[0]
        c, d = matrix.matrix[1]
        return (a*d)-(c*b)

    det = 0
    mini_matrix = mtx()
    for i in range(matrix.rows):
        mini_matrix.set_matrix(matrix.matrix)
        mini_matrix.remove_row(0)
        mini_matrix.remove_col(i)
        tmp = (matrix.matrix[0][i] * ((-1)**(i)) * determinant(mini_matrix))
        det += tmp
    return det