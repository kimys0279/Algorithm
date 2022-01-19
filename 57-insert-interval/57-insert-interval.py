class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        ans = []
        
        for i in intervals:
            if len(ans) == 0 or i[0] > ans[-1][-1]:
                ans.append(i)
        
            elif i[0] <= ans[-1][-1]:
                ans[-1][-1] = max(ans[-1][-1], i[-1])
                
        return ans