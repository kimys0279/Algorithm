class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            hh, mm = time.split(':')
            return int(hh)*60 + int(mm)
        
        times = []
        for i in timePoints:
            times.append(convert(i))
        
        times.sort()
        
        res = 1440 + times[0] - times[len(times) - 1]
        
        for i in range(1, len(times)):
            res = min(res, (times[i] - times[i-1]))
            
        return res