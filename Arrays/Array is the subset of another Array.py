def isSubset(arr1,arr2,m,n):
    i=0
    j=0
    for i in range(n):
        for j in range(m):
            if (arr2[i]==arr1[j]):
                break
        if (j==m):
            return 0
    return 1
arr1=[1,2,3,4,5,6]
arr2=[2,3,4]
m=len(arr1)
n=len(arr2)
if isSubset(arr1,arr2,m,n):
    print("arr2[] is subset of arr1[]")
else:
    print("arr2[] is not a subset of arr1[]")
