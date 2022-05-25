class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_int_32 = 2 ** 31
        
        s = s.strip()
        
        if len(s) == 0:
            return 0
        
        sign = 1
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        
        res = 0
        for i in s:
            if i.isnumeric():
                res = res*10 + (ord(i)-ord("0"))
            else:
                break
                
        res = sign*res
        if res <= -min_int_32:
            return -min_int_32
        elif res >= min_int_32-1:
            return min_int_32-1
        
        return res
                
                
            
        