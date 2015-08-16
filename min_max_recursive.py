#Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops
def minmax(data):
    def minmax(data,left,right):
        if left >= right - 1:
            return min(data[left],data[right]),max(data[left],data[right])
        else:
            mid = (left+right)/2
            left_min,left_max = minmax(data,left,mid)
            right_min,right_max = minmax(data,mid,right)
            return min(left_min,right_min),max(left_max,right_max)
    return minmax(data,0,len(data)-1)
print minmax([3,4,6,1,4,6,10,21])
