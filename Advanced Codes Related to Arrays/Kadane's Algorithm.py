def fun(arr,l):
    max_so_far=max(arr)
    for i in range(l-1):
        s=arr[i]
        for j in range(i+1,l):
            s+=arr[j]
            if s>max_so_far:
                max_so_far=s
    return max_so_far
arr=[-2,-3,4,-1,-2,1,5,-3]
print(f"Largest contiguous subarray sum is: {fun(arr,len(arr))}")
