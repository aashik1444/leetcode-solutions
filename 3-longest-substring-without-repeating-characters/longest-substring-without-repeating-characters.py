class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        sett = set()
    
        for j in range(len(s)):

            while s[j] in sett:
                sett.remove(s[i])
                i += 1

            
            longest = max(longest, (j - i) + 1)
            sett.add(s[j])

        return longest