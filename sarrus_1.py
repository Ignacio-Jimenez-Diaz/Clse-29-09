#ITERATIVO
def sarrus_iterative(matrix):
    """
    Calcula la determinante de una matriz 3x3 usando la regla de Sarrus de manera iterativa.
    """
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("La matriz debe ser 3x3 para usar la regla de Sarrus.")
    
    # Suma de productos diagonales positivas: a11*a22*a33 + a12*a23*a31 + a13*a21*a32
    positive = (matrix[0][0] * matrix[1][1] * matrix[2][2] +
                matrix[0][1] * matrix[1][2] * matrix[2][0] +
                matrix[0][2] * matrix[1][0] * matrix[2][1])
    
    # Suma de productos diagonales negativas: a13*a22*a31 + a11*a23*a32 + a12*a21*a33
    negative = (matrix[0][2] * matrix[1][1] * matrix[2][0] +
                matrix[0][0] * matrix[1][2] * matrix[2][1] +
                matrix[0][1] * matrix[1][0] * matrix[2][2])
    
    return positive - negative