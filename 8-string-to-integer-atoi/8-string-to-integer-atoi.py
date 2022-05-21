class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        
        if len(s) == 0:
            return 0

        result = 0
        sign_multiplier = 1
        start = 0
        min_int_32 = 2 ** 31
        
        if s[0] == "-":
            sign_multiplier = -1
            start = 1
            
        if s[0] == "+":
            sign_multiplier = 1
            start = 1
            
        for i in range(start, len(s)):
            if not s[i].isnumeric():
                if result * sign_multiplier <= -min_int_32:
                    return -min_int_32
                elif result * sign_multiplier >= min_int_32-1:
                    return min_int_32-1
                else:
                    return result * sign_multiplier
                
            current_int = ord(s[i]) - ord("0") # Ascii values
            result = result * 10 + current_int
        
        if result * sign_multiplier <= -min_int_32:
            return -min_int_32
        elif result * sign_multiplier >= min_int_32-1:
            return min_int_32-1
        else:
            return result * sign_multiplier
        
        
                
            
        