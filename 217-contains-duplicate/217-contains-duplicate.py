class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        visited_list = []
        
        for i in nums:
            if i in visited_list:
                return True
            else:
                visited_list.append(i)
                
        return False
        