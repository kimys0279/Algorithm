class Solution:
    def fib(self, n: int) -> int:
        list = [0, 1]
        for i in range(2, n+1):
            list.append(list[i-1] + list[i-2])
        return list[n]