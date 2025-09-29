#RECURSIVO
def get_minor_matrix(matrix, row, col):
    """
    Obtiene la submatriz eliminando la fila 'row' y la columna 'col'.
    """
    return [[matrix[i][j] for j in range(len(matrix)) if j != col]
            for i in range(len(matrix)) if i != row]

def determinant_2x2(matrix):
    """
    Calcula la determinante de una matriz 2x2.
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def sarrus_recursive(matrix, depth=0):
    """
    Calcula la determinante de una matriz 3x3 de manera recursiva usando expansión por cofactores.
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser 3x3 para usar la regla de Sarrus recursiva.")
    
    # Caso base: para una matriz 3x3, expandimos por la primera fila
    det = 0
    for j in range(3):
        # Cofactor: (-1)^(0+j) * a[0][j] * det(submatriz)
        minor = get_minor_matrix(matrix, 0, j)
        cofactor = ((-1) ** j) * matrix[0][j] * determinant_2x2(minor)
        det += cofactor
    
    return det