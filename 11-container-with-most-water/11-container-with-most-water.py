class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        res = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            area = (right-left)*min(height[left], height[right])
            res = max(res, area)
            if height[left]<height[right]:
                left = left+1
            else:
                right = right-1
        return res
            
        