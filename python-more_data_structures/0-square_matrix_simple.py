#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matriz = []
    for i in range(len(matrix)):
        n = list(map(lambda x: x ** 2, matrix[i]))
        matriz.append(n)
    return matriz
