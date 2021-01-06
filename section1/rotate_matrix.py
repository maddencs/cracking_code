import math


def swap(matrix):
    n = len(matrix)
    max_padding = math.floor(n/2)
    i = 0
    while i < max_padding:
        swapper(matrix, i)
        i += 1

    return matrix


def swapper(matrix, padding):
    n = len(matrix)
    row = padding
    column = padding

    while column < n - padding - 1:
        while row < n - padding - 1:

            # left side
            tmp = matrix[n-column - 1][row]
            matrix[n-column-1][row] = matrix[row][column]

            # bottom side
            tmp2 = matrix[n-padding-1][n-column-1]
            matrix[n-padding-1][n-column-1] = tmp

            # right side
            tmp = matrix[column][n-padding-1]
            matrix[column][n-padding-1] = tmp2

            # top side
            matrix[row][column] = tmp

            row += 1
        column += 1


test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(swap(test1))