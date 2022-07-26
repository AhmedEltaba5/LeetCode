class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        mat_exploded = [i for sublist in mat for i in sublist]
        
        if r*c != len(mat_exploded):
            return mat
        
        out = []
        k = 0
        for i in range(r):
            tmp = []
            for j in range(len(mat_exploded)/r):
                tmp.append(mat_exploded[k])
                k+=1
            out.append(tmp)
        return out
                
        