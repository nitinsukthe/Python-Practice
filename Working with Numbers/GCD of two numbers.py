num1=36
num2=60
gcd=1
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        gcd=i
print(f"GCD of {num1} and {num2} is {gcd}")
