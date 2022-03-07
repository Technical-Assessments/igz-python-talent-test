# -*- coding: utf-8 -*-
from functools import reduce


def elements_sum(matrix: list) -> int:
    """
        Esta función devuelve la suma de todos los elementos de la matriz cuadrada dada
        :param matrix: matriz cuadrada
        :return: La suma de todos los elementos de la matriz
    """
    print(matrix)
    return reduce(lambda i, row: i +
                  reduce(lambda j, val: j + val, row, 0),
                  matrix,
                  0)


def diagonal_sum(matrix: list) -> int:
    """
    Esta función debe devolver la suma de los elementos de la diagonal principal
    de la matriz cuadrada dada
    :param matrix: matriz cuadrada
    :return: La suma de los elementos de la diagonal principal de la matriz
    """

    return reduce(lambda i, value: i + value,
                  (matrix[j][j] for j in range(len(matrix))),
                  0)
