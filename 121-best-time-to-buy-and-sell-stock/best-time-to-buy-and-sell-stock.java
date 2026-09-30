class Solution {
    public int maxProfit(int[] prices) {
        int profit  = 0;
        int mB = prices[0];
        for (int i : prices) {
            mB = Math.min(mB, i);
            profit = Math.max(profit, i - mB);
        }
        return profit;
    }
}