class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            result = max(odd, even, result, key=len)
        return result
            
        
    def helper(self,s,l,r):
        while l>=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        