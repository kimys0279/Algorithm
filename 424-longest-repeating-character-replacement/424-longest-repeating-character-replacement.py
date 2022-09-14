class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c_frequency = {}
        longest = 0
        
        for r in range(len(s)):
            
            if s[r] not in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1
            
            cells_count = r - l + 1
            
            if cells_count - max(c_frequency.values()) <= k:
                longest = max(longest, cells_count)
            
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        
        return longest