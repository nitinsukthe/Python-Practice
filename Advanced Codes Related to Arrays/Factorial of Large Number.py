def factorial(n):
    ans=1
    while n>1:
        ans*=n
        n-=1
    return ans
n=5
print(factorial(n))
