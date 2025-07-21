def kth_min_max(arr, k):
    arr = list(set(arr))
    arr.sort()
    n = len(arr)
    if k > n:
        print("K is larger than the number of unique elements.")
        return
    print(f"{k}rd minimum element is:", arr[k - 1])
    print(f"{k}rd maximum element is:", arr[n - k])
arr = [12, 3, 5, 7, 19, 5, 3, 12, 40]
k = 3
kth_min_max(arr, k)
