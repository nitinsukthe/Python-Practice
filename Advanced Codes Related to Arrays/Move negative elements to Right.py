# MOVE TO RIGHT
def find(arr):
    ans = []
    for i in arr:
        if i < 0:
            ans.append(i)
        if 0 in arr:
            ans.append(0)
    for i in arr:
        if i > 0:
            ans.append(i)
    ans=ans[::-1]
    print("Array after moving all the elements to right:", ans)
array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
find(array)
