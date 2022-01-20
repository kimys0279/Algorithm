class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        ans = []

        while True:
            #top go right
            ans.extend(matrix[top][x] for x in range(left, right + 1))
            top += 1
                
            if top > bottom:
                break
            
            #Right side go down
            ans.extend(matrix[y][right] for y in range(top, bottom + 1))
            right -= 1
                
            if left > right:
                break
            
            #Bottom side go left
            ans.extend(matrix[bottom][x] for x in range(right, left - 1, -1))
            bottom -= 1
                
            if top > bottom:
                break
            
            #Left side go up
            ans.extend(matrix[y][left] for y in range(bottom, top - 1, -1))
            left += 1
                
            if left > right:
                break
                    
        return ans
