def rearrange(arr):
    p=0
    b=0
    for i in range(len(arr)):
        if b==1:
            b-=1
        elif arr[i]<0:
            arr[i],arr[p]=arr[p],arr[i]
            if p>i:
                b+=1
            p+=2
    return arr
array=[2,3,-1,-4,6,-9]
print(f"After Rearranging: {rearrange(array)}")
