class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_vol = 0
        
        for i in range(len(height)-1, 0, -1):
            if height[l] > height[r]:
                max_vol = max(max_vol, i*height[r])
                r -= 1
            else:
                max_vol = max(max_vol, i*height[l])
                l += 1
        return max_vol