class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        map_dict = dict()
        map_dict['2'] = "abc"
        map_dict['3'] = "def"
        map_dict['4'] = "ghi"
        map_dict['5'] = "jkl"
        map_dict['6'] = "mno"
        map_dict['7'] = "pqrs"
        map_dict['8'] = "tuv"
        map_dict['9'] = "wxyz"
        
        res = []
        def backTrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for char in map_dict[digits[i]]:
                backTrack(i+1, curStr+char)
                
        if len(digits)>0:
            backTrack(0, "")
        return res
                
        
        
        
        