class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = prices[0]
        max_profit = 0

        for n in prices:
            max_profit = max(max_profit, n - i)
            i = min(i, n)
        return max_profit