class Solution(object):
    def topKFrequent(self, words, k):
        dict = {}
        
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        res = sorted(dict, key = lambda x: (-dict[x], x))
        return res[:k]