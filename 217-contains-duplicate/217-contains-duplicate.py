class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        unique_nums = set(nums)
        
        if len(unique_nums) == len(nums):
            # no duplicates
            return False
        return True
        