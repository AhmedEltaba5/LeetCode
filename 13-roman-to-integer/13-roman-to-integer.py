class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nums_dict = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        
        total = 0
        prev = 0
        current = 0
        
        for i in s:
            current = nums_dict[i]
            if prev < current:
                total = total + current -2*prev
                prev = current
            else:
                total = total + current
                prev = current
        
        return total
            
        