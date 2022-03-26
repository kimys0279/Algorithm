class Solution(object):
    def longestStrChain(self, words):
        s = set(words)
        memo = {}
        
        def rec(word):
            if word not in s: return 0
            if word in memo:
                return memo[word]
            else:
                N = len(word)
                mx = 0
                for i in range(N):
                    mx = max(mx, rec(word[:i]+word[i+1:])+1)
                memo[word] = mx
            return mx
        
        for w in words:
            rec(w)
        
        return max(memo.values())