class Solution(object):
    def merge1(self, intervals):
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x: x[0])
        ans = []
        
        for i in intervals:
            if (len(ans) == 0 or i[0] > ans[-1][1]):
                ans.append(i)
            elif (i[0] <= ans[-1][1]):
                ans[-1][1] = max(ans[-1][1], i[1])
        return ans
    
    
    
    
    
    
    
    
    
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x: x[0])
        ans = []
        
        for i in intervals:
            if len(ans) == 0 or ans[-1][1] < i[0]:
                ans.append(i)
            elif ans[-1][1] >= i[0]:
                ans[-1][1] = max(i[1], ans[-1][1])
        return ans
        
        