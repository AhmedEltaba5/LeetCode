import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        local_max=0
        global_max=-np.inf
        for i in range(len(nums)):
            local_max=max(nums[i],nums[i]+local_max)   #using kadanes algo
            if local_max>global_max:
                global_max=local_max
                
        return global_max
        
        