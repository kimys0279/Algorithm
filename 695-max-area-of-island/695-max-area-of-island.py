class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue, max_area = deque([]), 0
        
        def bfs(queue):
            cur_area = 1
            while queue:
                x, y = queue.popleft()
                for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if 0<=nx<row and 0<=ny<col and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        cur_area += 1
                        queue.append((nx, ny))
            return cur_area
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append((x, y))
                    max_area = max(max_area, bfs(queue))
        return max_area