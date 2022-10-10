class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numli = []
        for i in nums:
            numli.append(i ** 2)
        return sorted(numli)