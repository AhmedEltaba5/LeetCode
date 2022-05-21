class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # sort the list
        nums.sort()
        length = len(nums)
        
        result = []
        
        for i in range(length - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = length - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum < 0:
                    left = left + 1
                elif total_sum > 0:
                    right = right - 1
                else:
                    # append triple
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                        
                    left = left + 1
                    right = right - 1
                    
    
        return result
                    
        
        