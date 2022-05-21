class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return False
        
        subtract_dict = {}
        for i in range(len(nums)):
            if nums[i] in subtract_dict:
                return subtract_dict[nums[i]], i
            else:
                subtract_dict[target-nums[i]] = i
                
            
        