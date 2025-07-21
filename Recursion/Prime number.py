def Prime_Number(n, i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return Prime_Number(n,i+1)
n=971
if Prime_Number(n):
    print(f"Yes, {n} is prime")
else:
    print(f"No, {n} is not a prime")
