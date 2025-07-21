def ispalindrome(n):
    return str(n)==str(n)[::-1]
def largestPalindrome(arr,n):
    currentMax=-1
    for i in range(0,n,1):
        if (arr[i]>currentMax and ispalindrome(arr[i])):
            currentMax=arr[i]
    return currentMax
arr=[1,232,5545455,161]
n=len(arr)
print(largestPalindrome(arr,n))
