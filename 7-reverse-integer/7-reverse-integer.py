class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # we will use mod and integer division
        
        if x> 2**31-1 or x < (-2)**31:
            return 0
        
        # handle negative
        negative = 1
        if x < 0:
            x = x * -1
            negative = -1
        result = 0
        while x:
            right_digit = x%10
            result = result*10 + right_digit
            x = x // 10
            
        result = negative * result
        if result > 2**31-1 or result < (-2)**31:
            return 0
        return result
        