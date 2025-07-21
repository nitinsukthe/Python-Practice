def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged=[intervals[0]]
    for current in intervals[1:]:
        last=merged[-1]
        if current[0]<=last[1]:
            last[1]=max(last[1],current[1])
        else:
            merged.append(current)
    return merged
arr=[[1,3],[2,6],[8,10],[15,18],[18,20]]
print(merge(arr))
