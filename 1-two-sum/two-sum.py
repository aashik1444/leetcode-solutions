class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in hmap:
                return [hmap[d], i]
            hmap[n] = i
        return 