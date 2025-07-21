def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1  # Move left
        else:
            i += 1  # Move down
    return False
matrix = [[1, 4, 7, 11],
          [2, 5, 8, 12],
          [3, 6, 9, 16],
          [10, 13, 14, 17]]
x = 9
print("Element found?" , search_matrix(matrix, x))
