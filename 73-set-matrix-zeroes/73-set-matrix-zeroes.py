class Solution(object):
    def setZeroes(self, matrix):      
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        if not matrix:
            return []
        
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True
                    
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
        return matrix