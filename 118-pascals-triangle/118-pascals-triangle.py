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
                if i <= 1:
                    tmp.append(1)
                else:
                    if j==0 or j==i:
                        tmp.append(1)
                    else:
                        tmp.append(out[i-1][j-1]+out[i-1][j])
                    
            out.append(tmp)
        
        return out
        
        
        