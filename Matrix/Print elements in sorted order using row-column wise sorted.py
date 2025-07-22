Matrix=[[1,20,43,14],
        [50,69,17,81],
        [99,10,11,22],
        [13,54,95,16]]
arr=[]
x,n,m=0,4,4
for i in range(n):
    for j in range(m):
        arr.append(Matrix[i][j])
size=n*m
arr.sort()
for i in range(size):
    print(arr[i],end=" ")
