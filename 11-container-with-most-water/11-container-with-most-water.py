class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        l, r = 0, len(height) - 1
        for i in range(len(height) - 1, 0, -1):
            if height[l] >= height[r]:
                maxi = max(maxi, height[r]*i)
                r -= 1
            else:
                maxi = max(maxi, height[l]*i)
                l += 1       
        
        return maxi