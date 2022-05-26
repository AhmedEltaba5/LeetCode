class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # BackTracking and recursion
        
        map_dict = {"1": "", "2": "abc", "3": "def", "4":"ghi", "5":"jkl",
                   "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        result = []
        
        def backTrack(i, curStr):
            # base condition'
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            
            for char in map_dict[digits[i]]:
                backTrack(i+1, curStr+char)
            
        if digits:
            backTrack(0, "")
        
        return result
                
    
            
        