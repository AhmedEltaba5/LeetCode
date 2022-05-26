class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # we will use left and right pointers
        
        left = 0
        right = len(height)-1
        
        max_area = 0
        
        while left <= right:
            area = min(height[left], height[right]) * (right-left)
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
        
        
        
        
        