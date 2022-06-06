import numpy as np

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res_sum = float('-inf')
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum+nums[i])
            res_sum=  max(res_sum, curr_sum)
                
        return res_sum
        
        