class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        subtract_dict = {}
        for i in range(len(nums)):
            if nums[i] in subtract_dict:
                res = [subtract_dict[nums[i]], i]
                return res
            else:
                subtract_dict[target-nums[i]] = i
            
            
        