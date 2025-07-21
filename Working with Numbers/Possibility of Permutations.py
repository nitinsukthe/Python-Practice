def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact*=i
    return fact
    
n=int(input("Enter the number of people: "))
r=int(input("Enter the number of seats: "))

p=factorial(n)//factorial(n-r)

print(f"Total number of arrangements are: {p}")
