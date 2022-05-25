class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 1:
            return 1
        
        res = 0
        visited_dict = dict()
        start = 0
        
        for i in range(len(s)):
            if s[i] in visited_dict and visited_dict[s[i]] >= start:
                # common substring finished
                start = visited_dict[s[i]]+1
            else:
                res = max(res, i-start+1)
            visited_dict[s[i]] = i
                
        return res
                
                
        
        