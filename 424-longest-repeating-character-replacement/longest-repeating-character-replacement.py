class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use frequency array to identify which character is most frequent
        #window to be invalid -> window - max(freq) > k
        i = 0
        longest = 0
        freq = [0] * 26

        for j in range(len(s)):
            freq[ord(s[j]) - ord('A')] += 1
            while ((j - i) + 1) - max(freq) > k:
                freq[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            longest = max(longest, (j - i) + 1)
        
        return longest  