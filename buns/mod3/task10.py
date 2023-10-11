size = int(input())
matrix = [[j+1 for j in range(size)] for i in range(size)]

def transp_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(str(digit) for digit in row))

print_matrix(matrix)
print()
transposed_matrix = transp_matrix(matrix)
print_matrix(transposed_matrix)