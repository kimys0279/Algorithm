class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}        
        newword = []
        for i, c in enumerate(order):
            dic[c] = i
        
        for i in words:
            new = []
            for j in i:
                new.append(dic[j])
            newword.append(new)
        
        for i, j in zip(newword, newword[1:]):
            if i > j:
                return False
        
        return True