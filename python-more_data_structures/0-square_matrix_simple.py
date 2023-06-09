#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    matriz = []
    for i in matrix:
        n = list(map(lambda x: x ** 2, matrix[i]))
        matriz.append(n)
    return matriz
