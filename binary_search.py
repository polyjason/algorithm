def binary_search(data, target, low,high):
    if low == high:
        return low if target == data[low] else -1
    else:
        mid = (low+high)/2
        if data[mid] == target:
            return mid
        elif target> data[mid]:
            return binary_search(data,target,mid+1,high)
        else:
            return binary_search(data,target,low,mid-1)


dddd = [1,3,4,5,7,10]
print binary_search(dddd,3,0,len(dddd))
print binary_search(dddd,10,0,len(dddd))
print binary_search(dddd,2,0,len(dddd))


