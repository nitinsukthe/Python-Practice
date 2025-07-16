def check(array,length):
    for i in range(0,length):
        while array[i]%2==0:
            array[i]//=2
        while array[i]%3==0:
            array[i]//=3
    if array[i]!=array[0]:
        return False
    return True
array=[50,100,75]
length=len(array)
if check(array,length):
    print("Yes, all the elements of an array can be made equal")
else:
    print("No, all the elements of an array cannot be made equal")
