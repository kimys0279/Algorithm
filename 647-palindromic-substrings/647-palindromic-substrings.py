class Solution(object):
    def countSubstrings(self, s):
        if not s:
            return 1
        n = len(s)
        list = [[False for x in range(n)] for y in range(n)]
        cnt = 0
        
        for i in range(n):
            list[i][i] = True
            cnt += 1
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                list[i][i + 1] = True
                cnt += 1
                
        for i in range(3, n + 1):
            for j in range(n - i + 1):
                k = i + j - 1
                if list[j + 1][k - 1] and s[j] == s[k]:
                    list[j][k] = True
                    cnt += 1
        
        return cnt