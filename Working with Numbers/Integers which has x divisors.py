Number=7
Divisor=2
count=0
for i in range(1,Number+1):
    count_factors=0
    for j in range(1,i+1):
        if i%j==0:
            count_factors+=1
        else:
            pass
    if count_factors==Divisor:
        count+=1
print(count)
