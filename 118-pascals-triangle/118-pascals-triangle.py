class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        out = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                tmp.append(1)
            out.append(tmp)
            
        if len(out) <= 2:
            return out
        
        for i in range(2,len(out)):
            for j in range(1,len(out[i])-1):
                out[i][j] = out[i-1][j-1]+out[i-1][j]
                
        return out
                
        
        
        