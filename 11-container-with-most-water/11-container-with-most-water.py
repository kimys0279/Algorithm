class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxVol = 0
        
        for i in range(len(height)-1, 0, -1):
            if height[l] > height[r]:
                maxVol = max(maxVol, i*height[r])
                r -= 1
            else:
                maxVol = max(maxVol, i*height[l])
                l += 1
        return maxVol