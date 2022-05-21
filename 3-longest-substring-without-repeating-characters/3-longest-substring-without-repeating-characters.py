class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # using sliding window technique
        
        length = len(s)
        max_length = start = 0
        
        if length == 0:
            return 0
        
        map_chars = {}
        for i in range(length):
            if s[i] in map_chars and map_chars[s[i]] >= start:
                # repeated character
                start = map_chars[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            map_chars[s[i]] = i
                
        return max_length
            
    
        