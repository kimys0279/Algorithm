class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        li = []
        for i in range(len(digits)):
            num += digits[-(i+1)] * 10**i
        
        num += 1
        
        for _ in range(len(str(num))):
            li.append(num%10)
            num = num//10
        
        return li[::-1]
        