def removeDuplicates(arr,n):
    if n==0 or n==1:
        return n
    temp=list(range(n))
    j=0;
    for i in range(0,n-1):
        if arr[i]!=arr[i+1]:
            temp[j]=arr[i]
            j+=1
    temp[j]=arr[n-1]
    j+=1
    for i in range(0,j):
        arr[i]=temp[i]
    return j
arr=[10,20,20,30,40,40,40,50,50]
n=len(arr)
n=removeDuplicates(arr,n)
for i in range(n):
    print("%d"%(arr[i]),end=" ")
