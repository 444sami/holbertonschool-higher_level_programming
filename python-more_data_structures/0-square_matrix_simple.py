#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matriz_a = []
    matriz_b = []
    for i in matrix:
        matriz_a = list(map(lambda x: x*x, i))
        matriz_b.append(matriz_a)
    return matriz_b
