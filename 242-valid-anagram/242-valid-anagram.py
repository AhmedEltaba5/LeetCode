class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0)+1
            countT[t[i]] = countT.get(t[i], 0)+1
            
        for i in countS:
            if countS[i] != countT.get(i):
                return False
        return True
        
        """
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
        """
        