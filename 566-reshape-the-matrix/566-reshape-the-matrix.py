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
        
        res = [mat_exploded[i:i+c] for i in range(0, len(mat_exploded), c)]
        return res
                
        