class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
        
#         l, r = 0, len(nums)
        
#         while True:
#             mid = l + r // 2
            
#             if mid == target:
#                 return mid
            
#             elif mid > target:
#                 l = mid
            
#             else:
#                 r = mid