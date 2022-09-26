class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        pt1, pt2 = 0, 0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        
        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    ans.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            
            except IndexError:
                break
                
        return ans