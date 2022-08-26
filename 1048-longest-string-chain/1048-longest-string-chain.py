class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        
        words.sort(key = len)
        dic = {}
        
        for i in words:
            dic[i] = 1
            for j in range(len(i)):
                predecessor = i[:j] + i[j+1:]
                
                if predecessor in dic:
                    dic[i] = max(dic[i], 1 + dic[predecessor])
                    
        return max(dic.values())