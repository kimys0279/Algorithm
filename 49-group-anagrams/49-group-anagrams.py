class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def stringtolist(str):
            arr = [0] * 26
            for char in str:
                arr[ord(char) - ord('a')] += 1
            return tuple(arr)
        
        tup = {}
        ans = []
        
        for str in strs:
            li = stringtolist(str)
            if li in tup:
                ans[tup[li]].append(str)
            else:
                ans.append([str])
                tup[li] = len(ans) - 1
        return ans
    