n=int(input("Enter a number: "))
p=n
sum1=0
while n>0:
    sum1+=n%10
    n=n//10
if (p%sum1==0):
    print(f"{p} is a Harshad number")
else:
    print(f"{p} is not a Harshad number")
