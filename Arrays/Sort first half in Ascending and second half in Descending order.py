def printOrder(arr,n):
    arr.sort()
    for i in range(n//2):
        print(arr[i],end=" ")
    for j in range(n-1,n//2-1,-1):
        print(arr[j],end=" ")
arr=[1,12,3,4,7,-2]
n=len(arr)
printOrder(arr,n)
