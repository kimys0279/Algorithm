class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        max_height = len(height) - 1
        ans = 0
        
        for i in range(max_height, 0, -1):
            if height[left] < height[right]:
                ans = max(ans, i * height[left])
                left += 1
                
            else:
                ans = max(ans, i * height[right])
                right -= 1
        return ans