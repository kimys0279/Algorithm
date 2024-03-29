class Solution(object):
    def eraseOverlapIntervals1(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: (x[0], x[1]))
        cnt = 0
        loopend = intervals[0][1]
        
        for i in intervals[1:]:
            if i[0] < loopend:
                cnt += 1
                loopend = min(loopend, i[1])
            else:
                loopend = i[1]
        return cnt
    
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: (x[0], x[1]))
        cnt = 0
        loopend = intervals[0][1]
        
        for i in intervals[1:]:
            if i[0] < loopend:
                cnt += 1
                loopend = min(loopend, i[1])
            else:
                loopend = i[1]
        return cnt