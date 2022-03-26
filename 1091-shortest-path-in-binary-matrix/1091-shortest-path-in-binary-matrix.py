from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        # 1 0 0
        # 1 1 0
        # 1 1 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        
        if grid[0][0] == 0:
            q.append((1, (0, 0)))
            visited.add((0, 0))
            
        while q:
            steps, tmp = q.popleft()
            l, k = tmp[0], tmp[1]
            
            if(l, k) == (m-1, n-1):
                return steps
            
            for (i, j) in direc:
                new_l, new_k = l+i, k+j
                if 0 <= new_l < m and 0 <= new_k < n and grid[new_l][new_k] == 0 and (new_l, new_k) not in visited:
                    q.append((steps + 1, (new_l, new_k)))
                    visited.add((new_l, new_k))
                    
        return -1