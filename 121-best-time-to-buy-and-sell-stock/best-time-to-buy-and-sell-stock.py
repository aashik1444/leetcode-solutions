class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = prices[0]

        for n in prices:
            if n < i:
                i = n
            
            profit = n - i

            if profit > max_profit:
                max_profit = profit
        
        return max_profit