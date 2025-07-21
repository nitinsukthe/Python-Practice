def leftRotate(arr,d,n):
    if (d==0 or d==n):
        return
    i=d
    j=n-d
    while i!=j:
        if i<j:
            swap(arr,d-i,d+j-i,i)
            j-=i
        else:
            swap(arr,d-i,d,j)
            i-=j
    swap(arr,d-i,d,i)
def swap(arr,fi,si,d):
    for i in range(d):
        temp=arr[fi+i]
        arr[fi+i]=arr[si+i]
        arr[si+i]=temp
arr=[10,20,30,40,50,60,70]
leftRotate(arr,2,7)
for i in range(7):
    print(arr[i],end=" ")
