def rotate_matrix_clockwise_inplace(matrix):
    if not matrix or not matrix[0]:
        return
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
matrix1_inplace = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
print(f"\nOriginal Matrix 1 (In-place):\n{matrix1_inplace}")
rotate_matrix_clockwise_inplace(matrix1_inplace)
print(f"Rotated Matrix 1 (In-place):\n{matrix1_inplace}")
