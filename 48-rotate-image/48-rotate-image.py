class Solution(object):
    def rotate1(self, matrix):
        
        #reverse
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
            
        #transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    
    def rotate(self, matrix):
        l, r= 0, len(matrix) - 1
        
        #reverse
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
            
        #transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]