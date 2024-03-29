class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        ans = []
        
        for i in intervals:
            if len(ans) == 0 or ans[-1][1] < i[0]:
                ans.append(i)
            elif ans[-1][1] >= i[0]:
                ans[-1][1] = max(ans[-1][1], i[1])
        return ans