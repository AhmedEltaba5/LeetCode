class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        res = ""
        min_str = min(strs, key=len)
        for i in range(len(min_str)):
            tmp = 1
            for j in strs:
                if j[i] != min_str[i]:
                    tmp = 0
            if tmp:
                res = res + min_str[i]
            else:
                break
        return res
        