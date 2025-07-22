mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
arr=[]
for i in range(3):
    for j in range(3):
        arr.append(mat[i][j])
arr.sort()
print(f"Median of the given marix is: {arr[4]}")
