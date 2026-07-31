class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #get the window to be fixed as the same no.of s1. s1 shouldn't be larger than #s2. Get a frequency array for s1 and s2. s1 frequency array won't change. #Check for the frequency array to be the same, within the fixed sliding window. #Remove l part when window moves]
        if len(s1) > len(s2):
            return False
        freq_s1, freq_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        if freq_s1 == freq_s2:
            return True

        for i in range(len(s1), len(s2)):
            freq_s2[ord(s2[i]) - ord('a')] += 1
            freq_s2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if freq_s1 == freq_s2:
                return True

        return False

