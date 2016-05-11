class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=3:
            return 1*(n-1)
        elif n==4:
            return 4
        else:
            return 3* self.integerBreak(n-3) if n>6 else 3*(n-3)
s = Solution()
print s.integerBreak(10)
        
