class Solution(object):
    def maximumEvenSplit(self, finalSum):
        if not finalSum:
            return []
        if finalSum % 2 == 1:
            return []
        
        res = []
        sum = 0
        a = 2
        
        while finalSum > sum:
            sum += a
            res.append(a)
            a += 2
        
        if sum == finalSum:
            return res
        else:
            res.pop(res.index(sum - finalSum))
        
        return res