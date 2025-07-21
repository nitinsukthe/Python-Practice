from math import ceil
def median_of_two_arrays(l, array):
    if (l % 2) == 0:
        medium = l // 2
        median = (array[medium] + array[medium - 1]) / 2
        return median
    else:
        medium = ceil(l / 2)
        return array[medium - 1]
array1 = [1, 12, 15, 26, 38]
array2 = [2, 13, 17, 30, 45]
print("Array after merging and sorting :", end="")
array1 += array2
array1.sort()
print(array1)
ans = median_of_two_arrays(len(array1), array1)
print("Median :", int(ans))
