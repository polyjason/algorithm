def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        min_num = nums[0]
        num_dict = {}
        all_nums = set(nums)
        for n in nums:
            num_dict[n]=1
            if n <min_num:
                min_num = n
        max_count = 0
        for n in nums:
            print n
            if n not in all_nums:
                continue
            next = n+1
            count = 1
            while next in all_nums:
                count +=1
                all_nums.remove(next)
                next += 1
            count += num_dict.get(next,0)
            if count > max_count:
                max_count = count
            num_dict[n] = count
            all_nums.remove(n)
            print num_dict
        return max_count
print longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
