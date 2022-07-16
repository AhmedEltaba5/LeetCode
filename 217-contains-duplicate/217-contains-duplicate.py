class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dict_lst=[]
        k=0
        for item in nums:
            if item not in dict_lst:
                dict_lst.append(item)
                #dict[item]=k
                k += 1
            else:
                return True
        return False
        
        """
        unique_nums = set(nums)
        
        if len(unique_nums) == len(nums):
            # no duplicates
            return False
        return True
        """