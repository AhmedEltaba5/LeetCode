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
                res = max(res, i-start)
                start = visited_dict[s[i]]+1
                visited_dict[s[i]] = i
            else:
                visited_dict[s[i]] = i
                res = max(res, i-start+1)
                
        return res
                
                
        
        