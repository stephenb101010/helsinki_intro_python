def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])

    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy[i])):
            matrix[j][i] = matrix_copy[i][j]

'''
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

            #..or alternatively
            # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
'''