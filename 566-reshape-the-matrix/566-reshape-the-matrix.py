class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = sum(mat, [])
        ans = []
        
        
        if len(flat) != r*c:
            return mat
        
        else:
            for i in range(0, len(flat), c):
                ans.append(flat[i:i+c])
                
            return ans