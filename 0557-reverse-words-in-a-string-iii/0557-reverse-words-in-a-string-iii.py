class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for i in s.split(' '):
            i = i[::-1] + ' '
            ans += i
        ans = ans[:-1]
        return ans