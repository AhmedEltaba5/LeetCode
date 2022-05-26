class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        
        nums.sort()
        
        for i in range(len(nums)-2):
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            
            while left < right and left>i and right<len(nums):
                sum_nums = nums[i]+nums[left]+nums[right]
                if sum_nums > 0:
                    right = right-1
                elif sum_nums < 0:
                    left = left+1
                else:
                    # sum equals zero
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left = left+1
                    while left < right and nums[right]==nums[right-1]:
                        right = right-1
                    left = left+1
                    right = right-1
        return res
        