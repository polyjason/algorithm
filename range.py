#Given a sorted array of integers, find the starting and ending position of a given target value.

#Your algorithm's runtime complexity must be in the order of O(log n).

#If the target is not found in the array, return [-1, -1].

#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4].
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = []
        def search_first_match(nums,target,start,end):
            if target<nums[start]:
                return None
            if target>nums[end]:
                return None
            if start ==end:
               if nums[start] == target:
                   return start
               else:
                   return None
            mid = (start+end)/2
            if target == nums[mid]:
                return mid
            if target>nums[mid]:
               return search_first_match(nums,target,mid+1,end)
            else:
               return search_first_match(nums,target,start,mid)
        match = search_first_match(nums,target,0,len(nums)-1)
        print match
        if match == None:
            return [-1,-1]
        results = [match,match]
        idx = match -1
        while idx>=0:
            if nums[idx] == target:
                results[0] = idx
                idx -=1
            else:
                break
        idx = match + 1
        while idx<len(nums):
            if nums[idx] == target:
                results[1] = idx
                idx +=1
            else:
                break
        return results
s = Solution()
print s.searchRange([1,2,3],1)
