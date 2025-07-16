def sumOfMinAbsDifferences(arr,n):
    arr.sort()
    sum=0
    sum+=abs(arr[0]-arr[1])
    sum+=abs(arr[n-1]-arr[n-2])
    for i in range(1,n-1):
        sum+=min(abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1]))
    return sum;
arr=[2,5,4,3]
n=len(arr)
print(f"Requried Sum = {sumOfMinAbsDifferences(arr,n)}")
