def count(arr,n):
    mp=dict()
    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for x in mp:
        if mp[x]!=1:
            print(x)
arr=[10,20,30,10,40,50,10,20]
n=len(arr)
count(arr,n)
