class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in strs:
            alpha = [0] * 26
            for c in i:
                alpha[ord(c) - ord("a")] += 1

            hmap[tuple(alpha)].append(i)

        return list(hmap.values())