def next(arr):
    ans=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            a=arr[i]
            b=arr[j]
            if b>a and ans<b-a:
                ans=b-a
    return ans
def stock_price(arr,l):
    ans=0
    for i in range(l):
        for j in range(i+1,l):
            if arr[j]>arr[i]:
                a=arr[j]-arr[i]
                b=next(arr[j+1:])
                if ans<b+a:
                    ans=b+a
    return ans
price=[2,30,15,10,8,25,80]
print(f"Maximum profit is: {stock_price(price,len(price))}")
