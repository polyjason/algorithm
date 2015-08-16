class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        num = []
        nums1_index = 0
        nums2_index = 0
        while nums1_index <len(nums1) and nums2_index < len(nums2):
            if nums1[nums1_index] <= nums2[nums2_index]:
                num.append(nums1[nums1_index])
                nums1_index +=1
            else:
                num.append(nums2[nums2_index])
                nums2_index +=1
        if nums1_index <len(nums1):
            num.extend(nums1[nums1_index:])
        if nums2_index < len(nums2):
            num.extend(nums2[nums2_index:])
        return num[len(num)/2] if len(num)%2 ==1 else float(num[len(num)/2-1] + num[len(num)/2])/2
