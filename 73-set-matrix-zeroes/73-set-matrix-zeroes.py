class Solution(object):
    def setZeroes1(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        if not matrix:
            return []
        
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] == True
                    zeroes_row[col] == True
                    
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0
        return matrix
    
    
    def setZeroes(self, matrix):
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