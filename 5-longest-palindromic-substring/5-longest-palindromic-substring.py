class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        for i in range(len(s)):
            odd = self.getPalindrome(s, i, i)
            even = self.getPalindrome(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res
        
    def getPalindrome(self, s, start, end):
        while start>=0 and end<len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
                    
                
        
        
        
        