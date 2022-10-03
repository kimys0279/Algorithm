class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        num = inf
        ind = -1
        for i in points:
            if x == i[0] or y == i[1]:
                dist = abs(x-i[0]) + abs(y-i[1])
                if dist < num:
                    num = dist
                    ind = points.index(i)
                
        return ind