class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        ans = 0
        
        for i in range(len(height) - 1, 0, -1):
            if height[l] < height[r]:
                ans = max(ans, i * height[l])
                l += 1
            else:
                ans = max(ans, i * height[r])
                r -= 1
        return ans