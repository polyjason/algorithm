class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        results = []
        if k == 0:
            return results
        for end in range(k,len(nums)+1):
            results.append(max(nums[end-k:end]))
        return results
