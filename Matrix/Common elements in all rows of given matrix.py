def find(mat, N, M):
    for j in range(0, N):
        x, count = mat[0][j], 0

        for i in range(1, M):
            flag = 0
            for k in range(0, N):
                if x == mat[i][k]:
                    flag = 1
                    mat[i][k] = -1
                    break
            if flag == 1:
                count += 1
        if count == M - 1:
            print(x)
N, M = 4, 4
mat = [[10, 20, 30, 40],
       [15, 25, 35, 30],
       [27, 30, 37, 48],
       [32, 33, 39, 30]]
find(mat, N, M)
