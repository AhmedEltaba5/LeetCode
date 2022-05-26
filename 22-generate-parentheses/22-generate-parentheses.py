class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # solution with BackTrack
        result = []
        def backTrack(S='', left=0, right=0):
            if len(S) == 2*n:
                result.append("".join(S))
                return
            
            if left<n:
                #S+="("
                backTrack(S+"(", left+1,right)
                #S.pop()
            
            if right<left:
                #S+=")"
                backTrack(S+")",left,right+1)
                #S.pop()
                
        backTrack()
        return set(result)
        