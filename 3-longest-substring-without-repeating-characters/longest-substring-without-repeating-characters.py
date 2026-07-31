class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        sett = set()
        n = len(s)
        for j in range(n):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            w = (j - i) + 1
            longest = max(longest, w)
            sett.add(s[j])
        return longest