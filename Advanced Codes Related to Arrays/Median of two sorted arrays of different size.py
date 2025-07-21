from math import ceil
def median_of_two_arrays(len, array):
    if (len % 2) == 0:
        medium = len // 2
        median = (array[medium] + array[medium - 1]) / 2
        return median
    else:
        medium = ceil(len / 2)
        return array[medium - 1]
array1 = [2, 10, 12, 26]
array2 = [3, 6, 30, 78, 90]
print("After merging and sorting both array : ", end="")
array1 += array2
array1.sort()
print(array1)
ans = median_of_two_arrays(len(array1), array1)
print("Median :", ans)
