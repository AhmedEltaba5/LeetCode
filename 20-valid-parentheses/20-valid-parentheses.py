class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        map_parenthes = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for i in s:
            if i in "([{":
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                if stack.pop()!=map_parenthes[i]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        
        