def printDivisors(n,factors):
    i=1
    while i<=n:
        if n%i==0:
            factors.append(i)
        i=i+1
    return sum(factors)-n

if __name__=="__main__":
    number1,number2=6,28
    if int(printDivisors(number1,[])/number1)==int(printDivisors(number2,[])/number2):
        print(f"{number1},{number2} is a Friendly pair")
    else:
        print(f"{number1},{number2} is not a Friendly pair")
