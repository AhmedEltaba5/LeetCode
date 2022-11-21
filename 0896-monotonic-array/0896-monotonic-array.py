class Solution(object):
    def isMonotonic(self, A):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(A) <=1:
            return True
        
        inc = True
        dec = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                inc = False  
            elif A[i] < A[i+1]:
                dec = False
            
            # check if monotone case was broken
            if not (inc or dec):
                return False

        return inc or dec
        