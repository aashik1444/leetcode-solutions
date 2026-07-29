class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = set(nums)
        longest = 0
        
        for n in k:
            if n-1 not in k:
                next_num = n + 1
                length = 1
                while next_num in k:
                    length += 1
                    next_num += 1
                    
                longest = max(longest, length)
        return longest