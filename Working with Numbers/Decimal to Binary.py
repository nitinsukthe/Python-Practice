def ConverttoBinary(num):
    binaryArray=[]
    while num>0:
        binaryArray.append(num%2)
        num=num//2
    for j in binaryArray:
        print(j,end="")
decimal_num=21
ConverttoBinary(decimal_num)
