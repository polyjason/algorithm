class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_dict = {}
        import math
        import numpy as np
        def numSquare(n):
            if n in dp_dict:
                return dp_dict[n]
            max_number = int(math.sqrt(n))
            if max_number ==1:
                dp_dict[n] = n
                return n
            elif max_number **2 ==n:
                dp_dict[n] = 1
                return 1
            else:
                dp_dict[n] = min([1+numSquare(n-i**2) for i in range(max_number,1,-1)])
                return dp_dict[n]
        x = numSquare(n)
        return x
s = Solution()
print s.numSquares(9975)
        
