class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high - low == 1:
            return 1
        if high == low and high % 2 == 1:
            return 1
        if low%2 == 1 and high%2 == 1:
            return (high-low)//2 + 1
        if (low%2 == 1 and high%2 != 1) or (low%2 != 1 and high%2 == 1):
            return (high-low+1)//2
        if low%2 != 1 and high%2 != 1:
            return (high-low)//2