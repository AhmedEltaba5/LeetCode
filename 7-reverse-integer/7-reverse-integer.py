class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>= (2**31)-1 or x <= (-2)**31:
            return 0
        
        sign = 1
        
        if x<0:
            sign = -1
            x = x * -1
        
        res = 0
        while x:
            res = res*10 + x%10
            x = x//10
        
        res = sign*res
        
        if res>= (2**31)-1 or res <= (-2)**31:
            return 0
        
        return res
        
        
        