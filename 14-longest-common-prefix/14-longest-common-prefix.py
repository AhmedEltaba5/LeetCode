class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        com_prefix = ""
        
        min_elm = min(strs)
        
        if min_elm == "":
            return com_prefix
        
        for i in range(len(min_elm)):
            char = min_elm[i]
            for item in strs:
                if item[i] != char:
                    return com_prefix
            com_prefix += char
        return com_prefix
                
            
        