def find(array1,array2,n1,n2):
    for i in array2:
        array1.append(i)
    array1=list(set(sorted(array1)))
    array2=array1[len(array1)-n2:]
    array1=array1[:len(array1)-n2]
    print("After:")
    print(f"Array1: {array1} \nArray2: {array2}")
array1=[1,2,3,5,8,9,10,13,15,20]
array2=[2,3,8,13]
print("Before: ")
print(f"Array1: {array1} \nArray2: {array2}")
find(array1,array2,len(array1),len(array2))
