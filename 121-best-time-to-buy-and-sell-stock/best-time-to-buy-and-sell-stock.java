class Solution {
    public int maxProfit(int[] prices) {
       int p = 0;
       int l = prices[0];
       for (int i : prices) {
            p = Math.max(p, i - l);
            l = Math.min(i, l);
       }
       return p; 
    }
}