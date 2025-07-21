from collections import Counter
def find_elements(arr,k):
    n=len(arr)
    freq=Counter(arr)
    result=[]
    for key,count in freq.items():
        if count>n//k:
            result.append(key)
    return result
arr=[3,1,2,2,1,2,3,3]
k=4
print(f"Elements appearing more than n/k times: {find_elements(arr,k)}")
