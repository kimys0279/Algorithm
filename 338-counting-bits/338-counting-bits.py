class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        arr = [0] * (n + 1)
        arr[0] = 0
        arr[1] = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr[i] = arr[i/2]
            else:
                arr[i] = 1 + arr[(i - 1) / 2]
                
        return arr
        